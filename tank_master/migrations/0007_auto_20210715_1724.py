# Generated by Django 3.2.4 on 2021-07-15 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank_master', '0006_auto_20210715_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank',
            name='oil_lit_closing',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
        migrations.AddField(
            model_name='tank',
            name='oil_lit_opening',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value should not be less than 0')]),
        ),
    ]
