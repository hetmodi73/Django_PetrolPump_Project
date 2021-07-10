from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class nozzlle(models.Model):
    date=models.DateField(default=datetime.utcnow)
    nozzlle_no=models.IntegerField()
    choice= (
        ('petrol','petrol'),
        ('Diesel','Diesel')
    )
    nozzlle_type=models.CharField(max_length=20,choices=choice)
    remark=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.nozzlle_no}"

    def get_absolute_url(self):
        return reverse('nozzlle-view')
