from django.db import models
from django.urls import reverse
from datetime import datetime
from django.core.validators import MinValueValidator
# Create your models here.

class dailybase_a(models.Model):
    date=models.DateField(default=datetime.utcnow)
    employee_id=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    employee_name=models.CharField(max_length=30)
    amount=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    remark=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.employee_id}-{self.amount}"

    def get_absolute_url(self):
        return reverse('e_dailybase_amount-view')

