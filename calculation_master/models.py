from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class calculation(models.Model):
    date=models.DateField(default=datetime.utcnow)
    tank_opening=models.IntegerField()
    tank_closing=models.IntegerField()
    total_lit_petrol=models.IntegerField()
    total_lit_diesel=models.IntegerField()
    loss_in_petrol=models.IntegerField()
    loss_in_diesel=models.IntegerField()

    def __str__(self):
        return f"({self.date})"

    def get_absolute_url(self):
        return reverse('calculation-view')

