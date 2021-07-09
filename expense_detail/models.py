from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class expense(models.Model):
    date=models.DateField(default=datetime.utcnow)
    tea_coffee=models.IntegerField()
    electricity=models.IntegerField()
    water_bill=models.IntegerField()
    stationary=models.IntegerField()
    labour_expense=models.IntegerField()
    property_tax=models.IntegerField()
    remark=models.TextField(max_length=100)

    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):
        return reverse('expense_detail-view')

