# Generated by Django 3.2.4 on 2021-07-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_master', '0007_auto_20210713_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile'),
        ),
    ]
