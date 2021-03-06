# Generated by Django 3.2.4 on 2021-07-13 08:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_payment', '0003_payment_slip_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cheque_no',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reffrence',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
    ]
