from django.db import models
from datetime import datetime
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.

class calculation(models.Model):
    date=models.DateField(default=datetime.utcnow)
    tank_opening=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    tank_closing=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_lit_petrol=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    total_lit_diesel=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_in_petrol=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    loss_in_diesel=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])

    def __str__(self):
        return f"({self.date})"

    def get_absolute_url(self):
        return reverse('calculation-view')

