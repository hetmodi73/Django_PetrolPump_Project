from django.db import models
from datetime import datetime
from vehicle_master.models import vehicle
from nozzlle_master.models import nozzlle
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.shortcuts import render
# Create your models here.

class creditor_transaction(models.Model):
    date=models.DateField(default=datetime.utcnow)
    vehicle_master=models.ForeignKey(vehicle,on_delete=models.CASCADE, related_name='creditor_transaction')
    nozzlle_master=models.ForeignKey(nozzlle,on_delete=models.CASCADE, related_name='creditor_transaction')
    petrol_in_lit=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    diesel_in_lit=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    petrol_price=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    diesel_price=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    remark=models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"({self.vehicle_master})-({self.nozzlle_master})"

    def get_absolute_url(self):
        return reverse('creditor_transaction-view')

def print_page(request, id):
    object = creditor_transaction.objects.get(id=id)
    return render(request, "creditors_transaction/print.html", {
    "object": object
    })
