from django.db import models
from django.urls import reverse
from django .core.validators import MinValueValidator
from datetime import datetime
# Create your models here.

class rate(models.Model):
    date=models.DateField(default=datetime.utcnow)
    petrol_price=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    diesel_price=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])

    def __str__(self):
        return f"petrol({self.petrol_price})-diesel({self.diesel_price})"

    def get_absolute_url(self):
        return reverse('rate-view')