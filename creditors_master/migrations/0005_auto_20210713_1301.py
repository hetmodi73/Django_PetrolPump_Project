# Generated by Django 3.2.4 on 2021-07-13 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_master', '0004_alter_creditors_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='contact_person_mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='gst_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='home_no',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='office_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='pending_balance',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AlterField(
            model_name='creditors',
            name='pincode',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
    ]
