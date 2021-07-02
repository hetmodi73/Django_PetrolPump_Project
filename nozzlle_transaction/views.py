from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import nozzlle_t
# Create your views here.

class NewNozzlle_tView(CreateView):
    model = nozzlle_t
    fields = '__all__'

class ListNozzlle_tView(ListView):
    model = nozzlle_t
    context_object_name = 'nozzlle_transaction'

class DeleteNozzlle_tView(DeleteView):
    model = nozzlle_t
    success_url = '/nozzlle_transaction/view'

class UpdateNozzlle_tView(UpdateView):
    model = nozzlle_t
    fields = '__all__'

class DetailNozzlle_tView(DetailView):
    model = nozzlle_t
    success_url = '/nozzlle_transaction/view'

