from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import employee
# Create your views here.

class NewEmployeeView(CreateView):
    model = employee
    fields = '__all__'

class ListEmployeeView(ListView):
    model = employee
    context_object_name = 'employee_payment'

class DeleteEmployeeView(DeleteView):
    model = employee
    success_url = '/employee_payment/view'

class UpdateEmployeeView(UpdateView):
    model = employee
    fields = '__all__'

class DetailEmployeeView(DetailView):
    model = employee
    success_url = '/employee_payment/view'

