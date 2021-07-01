from django.db import models
from django.urls import reverse
from django .core.validators import MinValueValidator
from datetime import datetime
# Create your models here.

class employee(models.Model):
    date=models.DateField(default=datetime.utcnow)
    employee_id=models.IntegerField()
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    Contact_no=models.IntegerField()
    address=models.CharField(max_length=20)
    Street=models.CharField(max_length=20)
    area=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    Country=models.CharField(max_length=20)
    dob=models.DateField()
    designation=models.CharField(max_length=20)
    choice1=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    gender=models.CharField(max_length=20,choices=choice1)
    reffrence=models.CharField(max_length=20)
    choice2=(
        ('Day-Shift', 'Day-Shift'),
        ('AfterNoon-Shift', 'AfterNoon-Shift'),
        ('Night-Shift', 'Night-Shift')
    )
    shift_timming=models.CharField(max_length=20,choices=choice2)
    education=models.CharField(max_length=20)
    Date_of_join=models.DateField()
    expected_salary=models.IntegerField()
    photo=models.ImageField(default='default.jpg',upload_to='profile')
    Document_file = models.FileField(blank=True,null=True,upload_to='profile')
    bank_name=models.CharField(max_length=20,null=True,blank=True)
    account_no=models.IntegerField(blank=True,null=True)
    ifsc_code=models.IntegerField(blank=True,null=True)
    salary=models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0,'Salary should not be less than 0')])
    Pan_Number=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"({self.employee_id})-({self.first_name} {self.middle_name} {self.last_name})-({self.salary})"

    def get_absolute_url(self):
        return reverse('employee-view')
