from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import suppliers
# Create your views here.

class NewSuppliersView(CreateView):
    model = suppliers
    fields = '__all__'

class ListSuppliersView(ListView):
    model = suppliers
    context_object_name = 'suppliers_master'

class DeleteSuppliersView(DeleteView):
    model = suppliers
    success_url = '/suppliers_master/view'

class UpdateSuppliersView(UpdateView):
    model = suppliers
    fields = '__all__'

class DetailSuppliersView(DetailView):
    model = suppliers
    success_url = '/suppliers_master/view'

