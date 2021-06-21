from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
# Create your views here.
from .models import employee

class NewEmployeeView(CreateView):
    model = employee
    fields = '__all__'
    template_name = "employee_master/employee_form.html"

class ListEmployeeView(ListView):
    model = employee
    context_object_name = 'employee_master'

class DeleteEmployeeView(DeleteView):
    model = employee
    success_url = '/employee_master/view'

class UpdateEmployeeView(UpdateView):
    model = employee
    fields = '__all__'
    success_url = '/employee_master/view'

class DetailEmployeeView(DetailView):
    model = employee
    fields = '__all__'
    success_url = '/employee_master/view'