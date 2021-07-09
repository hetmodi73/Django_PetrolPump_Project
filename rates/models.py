from django.db import models
from django.urls import reverse
from django .core.validators import MinValueValidator
from datetime import datetime
# Create your models here.

class rate(models.Model):
    date=models.DateField(default=datetime.utcnow)
    petrol_price=models.FloatField(validators=[MinValueValidator(0,'Price should not be less than 0')],null=True,blank=True)
    diesel_price=models.FloatField(validators=[MinValueValidator(0,'Price should not be less than 0')],null=True,blank=True)
    oil_stock=models.FloatField(validators=[MinValueValidator(0, 'Price should not be less than 0')],null=True,blank=True)

    def __str__(self):
        return f"petrol({self.petrol_price})-diesel({self.diesel_price})"

    def get_absolute_url(self):
        return reverse('rate-view')