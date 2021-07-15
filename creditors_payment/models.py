from django.db import models
from datetime import datetime
from creditors_master.models import creditors
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

class payment(models.Model):
    date=models.DateField(default=datetime.utcnow)
    creditors_master=models.ForeignKey(creditors,on_delete=models.CASCADE, related_name='payment')
    amount=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    choice1=(
        ('Cash','Cash'),
        ('Banking Transaction','Banking Transaction'),
        ('PhonePay','PhonePay'),
        ('GooglePay','GooglePay'),
        ('Paytm', 'Paytm'),
        ('UPI', 'UPI')
    )
    payment_type=models.CharField(max_length=50,choices=choice1)
    bank_name=models.CharField(max_length=50,null=True,blank=True)
    branch_name=models.CharField(max_length=50,null=True,blank=True)
    cheque_no=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    cheque_date=models.DateField(default=datetime.utcnow,null=True,blank=True)
    reffrence=models.IntegerField(default=0,null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    slip_no=models.CharField(max_length=20,default=0,null=True,blank=True)

    def __str__(self):
        return f"{self.creditors_master}-{self.amount}"

    def get_absolute_url(self):
        return reverse('creditors_payment-view')

