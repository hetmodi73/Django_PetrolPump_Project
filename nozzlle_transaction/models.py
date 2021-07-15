from django.db import models
from datetime import datetime
from nozzlle_master.models import nozzlle
from employee_master.models import employee
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

class nozzlle_t(models.Model):
    date=models.DateField(default=datetime.utcnow)
    nozzlle_master=models.ForeignKey(nozzlle,on_delete=models.CASCADE, related_name='nozzlle_t')
    employee_master=models.ForeignKey(employee,on_delete=models.CASCADE, related_name='nozzlle_t')
    cash=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    phonePay=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    googlePay=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    paytm=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    upi=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    credit_debit_card=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_lit_petrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_lit_diesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_price_petrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_price_diesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_price_petrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_price_diesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    opening_time=models.TimeField(null=True,blank=True)
    closing_time=models.TimeField(null=True,blank=True)
    opening_lit_petrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    closing_lit_petrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    Opening_lit_Diesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    closing_lit_Diesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    creditor_amount=models.FloatField(default=0,validators=[MinValueValidator(0,'Value should not be less than 0')])

    def __str__(self):
        return f"{self.nozzlle_master}-{self.employee_master}"

    def get_absolute_url(self):
        return reverse('nozzlle_transaction-view')

