from django.db import models
from datetime import datetime
from nozzlle_master.models import nozzlle
from employee_master.models import employee
from django.urls import reverse
# Create your models here.

class nozzlle_t(models.Model):
    date=models.DateField(default=datetime.utcnow)
    nozzlle_master=models.ForeignKey(nozzlle,on_delete=models.CASCADE, related_name='nozzlle_t')
    employee_master=models.ForeignKey(employee,on_delete=models.CASCADE, related_name='nozzlle_t')
    cash=models.IntegerField(null=True,blank=True)
    phonePay=models.IntegerField(null=True,blank=True)
    googlePay=models.IntegerField(null=True,blank=True)
    paytm=models.IntegerField(null=True,blank=True)
    upi=models.IntegerField(null=True,blank=True)
    credit_debit_card=models.IntegerField(null=True,blank=True)
    total_lit_petrol=models.IntegerField(null=True,blank=True)
    total_lit_diesel=models.IntegerField(null=True,blank=True)
    total_price_petrol=models.IntegerField(null=True,blank=True)
    total_price_diesel=models.IntegerField(null=True,blank=True)
    loss_price_petrol=models.IntegerField(null=True,blank=True)
    loss_price_diesel=models.IntegerField(null=True,blank=True)
    opening_time=models.TimeField(null=True,blank=True)
    closing_time=models.TimeField(null=True,blank=True)
    opening_lit_petrol=models.IntegerField(null=True,blank=True)
    closing_lit_petrol=models.IntegerField(null=True,blank=True)
    Opening_lit_Diesel=models.IntegerField(null=True,blank=True)
    closing_lit_Diesel=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.nozzlle_master}-{self.employee_master}"

    def get_absolute_url(self):
        return reverse('nozzlle_transaction-view')

