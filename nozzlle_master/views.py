from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import nozzlle
from django.http.response import JsonResponse
from datetime import datetime
# Create your views here.

class NewNozzlleView(CreateView):
    model = nozzlle
    fields = '__all__'

class ListNozzlleView(ListView):
    model = nozzlle
    context_object_name = 'nozzlle_master'

class DeleteNozzlleView(DeleteView):
    model = nozzlle
    success_url = '/nozzlle_master/view'

class UpdateNozzlleView(UpdateView):
    model = nozzlle
    fields = '__all__'

class DetailNozzlleView(DetailView):
    model = nozzlle
    success_url = '/nozzlle_master/view'

def type_of_nozzlle(request,nid):
    type=nozzlle.objects.get(id=nid).nozzlle_type
    return JsonResponse({"type":type})

def get_creditor_lit_by_nozzle(request,nid):
    from django.db.models import Sum
    noz=nozzlle.objects.get(id=nid)
    print(datetime.utcnow().date())
    if noz.nozzlle_type.lower()=='petrol':
        data=noz.creditor_transaction.filter(date=datetime.utcnow().date()).aggregate(Sum('petrol_in_lit'))

    else:
        data=noz.creditor_transaction.filter(date=datetime.utcnow().date()).aggregate(Sum('diesel_in_lit'))

    return JsonResponse(data)