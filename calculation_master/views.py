from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import calculation
# Create your views here.

class NewCalculationView(CreateView):
    model = calculation
    fields = '__all__'

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

