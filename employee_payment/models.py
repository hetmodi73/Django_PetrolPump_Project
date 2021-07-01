from django.db import models
from datetime import datetime
from employee_master.models import employee
from django.urls import reverse
# Create your models here.

class employee(models.Model):
    date=models.DateField(default=datetime.utcnow)
    employee_master=models.ForeignKey(employee,on_delete=models.CASCADE, related_name='employee')
    amount_dailybase=models.IntegerField(null=True,blank=True)
    choice1=(
        ('Cash', 'Cash'),
        ('Banking Transaction', 'Banking Transaction'),
        ('PhonePay', 'PhonePay'),
        ('GooglePay', 'GooglePay'),
        ('Paytm', 'Paytm'),
        ('UPI', 'UPI')
    )
    payment_type=models.CharField(max_length=30,choices=choice1)
    bank_name=models.CharField(max_length=50, null=True, blank=True)
    branch_name=models.CharField(max_length=50, null=True, blank=True)
    ifsc_code=models.IntegerField(null=True, blank=True)
    cheque_no=models.IntegerField(null=True, blank=True)
    cheque_date=models.DateField(default=datetime.utcnow, null=True, blank=True)
    reffrence=models.IntegerField(default=0, null=True, blank=True)
    salary=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"({self.employee_master})-({self.salary})"

    def get_absolute_url(self):
        return reverse('employee_payment-view')
