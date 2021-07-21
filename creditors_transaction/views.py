from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import creditor_transaction
# Create your views here.

class NewCreditor_transactionView(CreateView):
    model = creditor_transaction
    fields = '__all__'

class ListCreditor_transactionView(ListView):
    model = creditor_transaction
    context_object_name = 'creditors_transaction'

class DeleteCreditor_transactionView(DeleteView):
    model = creditor_transaction
    success_url = '/creditors_transaction/view'

class UpdateCreditor_transactionView(UpdateView):
    model = creditor_transaction
    fields = '__all__'

class DetailCreditor_transactionView(DetailView):
    model = creditor_transaction
    success_url = '/creditors_transaction/view'

class DetailCreditor_transactionView(DetailView):
    model = creditor_transaction
