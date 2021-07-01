from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class suppliers(models.Model):
    date = models.DateField(default=datetime.utcnow)
    receipt_no=models.IntegerField()
    petrol_in_lit=models.IntegerField()
    diesel_in_lit=models.IntegerField()
    loss_of_petrol_in_lit=models.IntegerField()
    loss_of_diesel_in_lit=models.IntegerField()
    transportation_expense=models.IntegerField()

    def __str__(self):
        return f"{self.date}-{self.receipt_no}"

    def get_absolute_url(self):
        return reverse('suppliers_master-view')
