# Generated by Django 3.2.4 on 2021-07-20 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nozzlle_transaction', '0007_auto_20210713_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nozzlle_t',
            name='Opening_lit_Diesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='cash',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='closing_lit_Diesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='closing_lit_petrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='credit_debit_card',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='googlePay',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='loss_price_diesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='loss_price_petrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='opening_lit_petrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='paytm',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='phonePay',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_lit_diesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_lit_petrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_price_diesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_price_petrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='upi',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
    ]
