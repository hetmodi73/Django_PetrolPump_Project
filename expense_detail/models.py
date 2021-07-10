from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class expense(models.Model):
    date=models.DateField(default=datetime.utcnow)
    tea_coffee=models.IntegerField(null=True,blank=True)
    electricity=models.IntegerField(null=True,blank=True)
    water_bill=models.IntegerField(null=True,blank=True)
    stationary=models.IntegerField(null=True,blank=True)
    labour_expense=models.IntegerField(null=True,blank=True)
    property_tax=models.IntegerField(null=True,blank=True)
    maintainence_expense=models.IntegerField(null=True,blank=True)
    machinory_expense=models.IntegerField(null=True,blank=True)
    insurence_expence=models.IntegerField(null=True,blank=True)
    ruff_expense=models.IntegerField(null=True,blank=True)
    employee_insurance_expense=models.IntegerField(null=True,blank=True)
    total_Amount = models.IntegerField(null=True,blank=True)
    remark=models.TextField(max_length=50,null=True,blank=True)


    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):
        return reverse('expense_detail-view')

