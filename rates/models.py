from django.db import models
from django.urls import reverse
# Create your models here.

class rate(models.Model):
    date=models.DateField()
    petrol_price=models.FloatField()
    diesel_price=models.FloatField()

    def __str__(self):
        return f"petrol({self.petrol_price})-diesel({self.diesel_price})"

    def get_absolute_url(self):
        return reverse('rate-view')