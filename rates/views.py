from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import rate
# Create your views here.

class NewRateView(CreateView):
    model = rate
    fields = '__all__'

class ListRateView(ListView):
    model = rate
    context_object_name = 'rates'

class DeleteRateView(DeleteView):
    model = rate
    success_url = '/rates/view'

class UpdateRateView(UpdateView):
    model = rate
    fields = '__all__'

class DetailRateView(DetailView):
    model = rate
