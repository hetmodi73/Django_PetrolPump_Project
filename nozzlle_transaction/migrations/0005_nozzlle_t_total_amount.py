# Generated by Django 3.2.4 on 2021-07-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nozzlle_transaction', '0004_auto_20210710_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='nozzlle_t',
            name='total_amount',
            field=models.FloatField(default=0),
        ),
    ]