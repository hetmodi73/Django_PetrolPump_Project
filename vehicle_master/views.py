from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import vehicle
# Create your views here.

class NewVehicleView(CreateView):
    model = vehicle
    fields = '__all__'

class ListVehicleView(ListView):
    model = vehicle
    context_object_name = 'vehicle_master'

class DeleteVehicleView(DeleteView):
    model = vehicle
    success_url = '/vehicle_master/view'

class UpdateVehicleView(UpdateView):
    model = vehicle
    fields = '__all__'

class DetailVehicleView(DetailView):
    model = vehicle
    success_url = '/vehicle_master/view'

