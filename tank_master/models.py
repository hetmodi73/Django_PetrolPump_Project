from django.db import models
from django.urls import reverse
# Create your models here.
from django .core.validators import MinValueValidator
class tank(models.Model):
    date=models.DateField()
    petrol_opening=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    petrol_closing=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    diesel_opening=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    diesel_closing=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    loss_petrol_lit=models.IntegerField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    loss_diesel_lit=models.IntegerField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    loss_petrol_price=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    loss_diesel_price=models.FloatField(validators=[MinValueValidator(0,'Salary should not be less than 0')])

    def __str__(self):
        return f"({self.petrol_opening})-({self.diesel_opening})"

    def get_absolute_url(self):
        return reverse('tank-view')
