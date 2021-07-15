from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.
from django .core.validators import MinValueValidator

class tank(models.Model):
    date=models.DateField(default=datetime.utcnow)
    petrol_opening=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    petrol_closing=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    diesel_opening=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    diesel_closing=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    loss_petrol_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    loss_diesel_lit=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    loss_petrol_price=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    loss_diesel_price=models.FloatField(validators=[MinValueValidator(0,'Value should not be less than 0')],null=True,blank=True)
    oil_lit_opening=models.FloatField(blank=True,null=True,validators=[MinValueValidator(0,'Value should not be less than 0')])
    oil_lit_closing = models.FloatField(blank=True, null=True,
                                        validators=[MinValueValidator(0, 'Value should not be less than 0')])

    def __str__(self):
        return f"({self.petrol_opening})-({self.diesel_opening})"

    def get_absolute_url(self):
        return reverse('tank-view')
