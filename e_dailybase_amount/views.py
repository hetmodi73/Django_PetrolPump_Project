from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import dailybase_a
# Create your views here.

class NewDailybase_aView(CreateView):
    model = dailybase_a
    fields = '__all__'

class ListDailybase_aView(ListView):
    model = dailybase_a
    context_object_name = 'e_dailybase_amount'

class DeleteDailybase_aView(DeleteView):
    model = dailybase_a
    success_url = '/e_dailybase_amount/view'

class UpdateDailybase_aView(UpdateView):
    model = dailybase_a
    fields = '__all__'

class DetailDailybase_aView(DetailView):
    model = dailybase_a
    success_url = '/e_dailybase_amount/view'

