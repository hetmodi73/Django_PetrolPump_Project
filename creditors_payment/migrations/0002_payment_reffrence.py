# Generated by Django 3.2.4 on 2021-06-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='reffrence',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
