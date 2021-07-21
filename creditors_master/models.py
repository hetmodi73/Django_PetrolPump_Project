from django.db import models
from django.urls import reverse
from django .core.validators import MinValueValidator
from datetime import datetime
from django.core.validators import MinValueValidator
# from django.shortcuts import render
# Create your models here.

class creditors(models.Model):
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile_no=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    office_no=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    contact_person_name=models.CharField(max_length=20)
    contact_person_mobile_no=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    company_name=models.CharField(max_length=20)
    home_no=models.CharField(max_length=20,)
    street_name=models.CharField(max_length=20)
    area_name=models.CharField(max_length=20)
    pincode=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    gst_no=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    pending_balance=models.IntegerField(validators=[MinValueValidator(0,'Value should not be less than 0')])
    creation_date=models.DateField(default=datetime.utcnow)

    def __str__(self):
        return f"({self.creation_date})-({self.company_name})"

    def get_absolute_url(self):
        return reverse('creditors-view')

# def print_page(request, id):
#     object = creditors.objects.get(id=id)
#     return render(request, "creditors_master/print.html", {
#     "object": object
#     })



