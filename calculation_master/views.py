from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import calculation
from nozzlle_transaction.models import nozzlle_t
from django.db.models import Sum
from datetime import datetime
from tank_master.models import tank
# Create your views here.

class NewCalculationView(CreateView):
    model = calculation
    fields = '__all__'

    def get_context_data(self, **kwargs):
        ctx = super(NewCalculationView, self).get_context_data(**kwargs)
        ctx["total_lit_petrol"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_lit_petrol'))['total_lit_petrol__sum']
        ctx["total_lit_diesel"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_lit_diesel'))['total_lit_diesel__sum']
        ctx["total_price_petrol"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_price_petrol'))['total_price_petrol__sum']
        ctx["total_price_diesel"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_price_diesel'))['total_price_diesel__sum']
        ctx["tank_lit_petrol"] = tank.objects.get(date=datetime.utcnow().date()).petrol_closing -tank.objects.get(date=datetime.utcnow().date()).petrol_opening
        ctx["tank_lit_diesel"] = tank.objects.get(date=datetime.utcnow().date()).diesel_opening -tank.objects.get(date=datetime.utcnow().date()).diesel_opening
        ctx["loss_price_petrol"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('loss_price_petrol'))['loss_price_petrol__sum']
        ctx["loss_price_diesel"] = nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('loss_price_diesel'))['loss_price_diesel__sum']
        return ctx

class ListCalculationView(ListView):
    model = calculation
    context_object_name = 'calculation_master'

class DeleteCalculationView(DeleteView):
    model = calculation
    success_url = '/calculation_master/view'

class UpdateCalculationView(UpdateView):
    model = calculation
    fields = '__all__'

class DetailCalculationView(DetailView):
    model = calculation
    success_url = '/calculation_master/view'

