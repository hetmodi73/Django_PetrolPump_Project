from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import nozzlle
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

