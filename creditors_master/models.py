from django.db import models
from django.urls import reverse
from django .core.validators import MinValueValidator
# Create your models here.

class creditors(models.Model):
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile_no=models.IntegerField()
    office_no=models.IntegerField()
    contact_person_name=models.CharField(max_length=20)
    contact_person_mobile_no=models.IntegerField()
    company_name=models.CharField(max_length=20)
    home_no=models.CharField(max_length=20)
    street_name=models.CharField(max_length=20)
    area_name=models.CharField(max_length=20)
    pincode=models.IntegerField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    gst_no=models.IntegerField()
    pending_balance=models.IntegerField(validators=[MinValueValidator(0,'Salary should not be less than 0')])
    creation_date=models.DateField()

    def __str__(self):
        return f"({self.creation_date})-({self.company_name})"

    def get_absolute_url(self):
        return reverse('creditors-view')