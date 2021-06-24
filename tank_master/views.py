from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import tank
from rates.models import rate
from django.http.response import JsonResponse
from datetime import datetime
# Create your views here.

class NewTankView(CreateView):
    model = tank
    fields = '__all__'

class ListTankView(ListView):
    model = tank
    context_object_name = 'tank_master'

class DeleteTankView(DeleteView):
    model = tank
    success_url = '/tank_master/view'

class UpdateTankView(UpdateView):
    model = tank
    fields = '__all__'

class DetailTankView(DetailView):
    model = tank
    success_url = '/tank_master/view'


def petrol_same_date_rate(request):
   petrolprice=rate.objects.get(date=datetime.utcnow().date()).petrol_price
   return JsonResponse({'petrol_price':petrolprice})

def diesel_same_date_rate(request):
   dieselprice=rate.objects.get(date=datetime.utcnow().date()).diesel_price
   return JsonResponse({'diesel_price':dieselprice})
