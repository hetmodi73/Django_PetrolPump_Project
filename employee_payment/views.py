from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import employee_p
# Create your views here.

class NewEmployee_pView(CreateView):
    model = employee_p
    fields = '__all__'
    template_name = "employee_payment/employee_p_form.html"

class ListEmployee_pView(ListView):
    model = employee_p
    context_object_name = 'employee_payment'

class DeleteEmployee_pView(DeleteView):
    model = employee_p
    success_url = '/employee_payment/view'

class UpdateEmployee_pView(UpdateView):
    model = employee_p
    fields = '__all__'

class DetailEmployee_pView(DetailView):
    model = employee_p
    success_url = '/employee_payment/view'

