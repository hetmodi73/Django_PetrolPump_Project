# Generated by Django 3.2.4 on 2021-06-25 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='diesel_closing',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='diesel_opening',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='loss_diesel_lit',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='loss_diesel_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='loss_petrol_lit',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='loss_petrol_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='petrol_closing',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='petrol_opening',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Salary should not be less than 0')]),
        ),
    ]
