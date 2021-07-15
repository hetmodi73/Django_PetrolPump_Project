from django.db import models
from datetime import datetime
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

class suppliers(models.Model):
    date = models.DateField(default=datetime.utcnow)
    receipt_no=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    petrol_in_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    diesel_in_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    oil_in_lit=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_of_petrol_in_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_of_diesel_in_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    transportation_expense=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])

    def __str__(self):
        return f"{self.date}-{self.receipt_no}"

    def get_absolute_url(self):
        return reverse('suppliers_master-view')

