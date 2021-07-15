from django.db import models
from django.urls import reverse
from creditors_master.models import creditors
from datetime import datetime
# Create your models here.

class vehicle(models.Model):
    date=models.DateField(default=datetime.utcnow)
    vehicle_no=models.CharField(max_length=20)
    driver_name=models.CharField(max_length=20)
    choice1=(
        ('2 wheeler','2 wheeler'),
        ('4 wheeler','4 wheeler'),
        ('6 wheeler','6 wheeler')
    )
    vehicle_type=models.CharField(max_length=20,choices=choice1)
    choice2=(
        ('Petrol','Petrol'),
        ('Diesel','Diesel')
    )
    fuel_type=models.CharField(max_length=20,choices=choice2)
    creditors_master=models.ForeignKey(creditors,on_delete=models.CASCADE, related_name='vehicle')
    remark=models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"({self.vehicle_no})-({self.creditors_master})"

    def get_absolute_url(self):
        return reverse('vehicle-view')

