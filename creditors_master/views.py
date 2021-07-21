from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import creditors
# Create your views here.

class NewCreditorsView(CreateView):
    model = creditors
    fields = '__all__'

class ListCreditorsView(ListView):
    model = creditors
    context_object_name = 'creditors_master'

class DeleteCreditorsView(DeleteView):
    model = creditors
    success_url = '/creditors_master/view'

class UpdateCreditorsView(UpdateView):
    model = creditors
    fields = '__all__'

class DetailCreditorsView(DetailView):
    model = creditors
    success_url = '/creditors_master/view'

class DetailCtransactionView(DetailView):
    model = creditors