# Generated by Django 3.2.4 on 2021-07-01 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_master', '0004_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
