# Generated by Django 3.2.4 on 2021-07-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditors_master', '0005_auto_20210713_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='home_no',
            field=models.CharField(max_length=20),
        ),
    ]
