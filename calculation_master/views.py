from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import calculation
from nozzlle_transaction.models import nozzlle_t
from django.db.models import Sum
from datetime import datetime
# Create your views here.

class NewCalculationView(CreateView):
    model = calculation
    fields = '__all__'
    extra_context = {"total_lit_petrol":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_lit_petrol'))['total_lit_petrol__sum'],
                     "total_lit_diesel":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('total_lit_diesel'))['total_lit_diesel__sum'],
                     "opening_lit_petrol":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('opening_lit_petrol'))['opening_lit_petrol__sum'],
                     "closing_lit_petrol":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('closing_lit_petrol'))['closing_lit_petrol__sum'],
                     "Opening_lit_Diesel":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('Opening_lit_Diesel'))['Opening_lit_Diesel__sum'],
                     "closing_lit_Diesel":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('closing_lit_Diesel'))['closing_lit_Diesel__sum'],
                     "loss_price_petrol":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('loss_price_petrol'))['loss_price_petrol__sum'],
                     "loss_price_diesel":nozzlle_t.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('loss_price_diesel'))['loss_price_diesel__sum']
                    }

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

