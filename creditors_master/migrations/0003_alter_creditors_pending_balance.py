# Generated by Django 3.2.4 on 2021-06-25 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_master', '0002_alter_creditors_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='pending_balance',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
    ]
