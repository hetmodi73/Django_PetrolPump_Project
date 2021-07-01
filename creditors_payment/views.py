from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import payment
# Create your views here.

class NewPaymentView(CreateView):
    model = payment
    fields = '__all__'

class ListPaymentView(ListView):
    model = payment
    context_object_name = 'creditors_payment'

class DeletePaymentView(DeleteView):
    model = payment
    success_url = '/creditors_payment/view'

class UpdatePaymentView(UpdateView):
    model = payment
    fields = '__all__'

class DetailPaymentView(DetailView):
    model = payment
    success_url = '/creditors_payment/view'

