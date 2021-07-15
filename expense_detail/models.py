from django.db import models
from datetime import datetime
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

class expense(models.Model):
    date=models.DateField(default=datetime.utcnow)
    tea_coffee=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    electricity=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    water_bill=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    stationary=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    labour_expense=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    property_tax=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    maintainence_expense=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    machinory_expense=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    insurence_expence=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    ruff_expense=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    employee_insurance_expense=models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_Amount = models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    remark=models.TextField(max_length=50,null=True,blank=True)


    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):
        return reverse('expense_detail-view')

