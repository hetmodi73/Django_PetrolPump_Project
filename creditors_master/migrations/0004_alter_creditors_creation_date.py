# Generated by Django 3.2.4 on 2021-07-10 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_master', '0003_alter_creditors_pending_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='creation_date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]