# Generated by Django 3.2.4 on 2021-07-01 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank_master', '0003_auto_20210625_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
