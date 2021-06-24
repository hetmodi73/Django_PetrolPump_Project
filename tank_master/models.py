from django.db import models
from django.urls import reverse
# Create your models here.

class tank(models.Model):
    date=models.DateField()
    petrol_opening=models.IntegerField()
    petrol_closing=models.IntegerField()
    diesel_opening=models.IntegerField()
    diesel_closing=models.IntegerField()
    loss_petrol_lit=models.IntegerField()
    loss_diesel_lit=models.IntegerField()
    loss_petrol_price=models.IntegerField()
    loss_diesel_price=models.IntegerField()

    def __str__(self):
        return f"({self.petrol_opening})-({self.diesel_opening})"

    def get_absolute_url(self):
        return reverse('tank-view')
