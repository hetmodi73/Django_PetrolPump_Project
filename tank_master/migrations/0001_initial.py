# Generated by Django 3.2.4 on 2021-06-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('petrol_opening', models.IntegerField()),
                ('petrol_closing', models.IntegerField()),
                ('diesel_opening', models.IntegerField()),
                ('diesel_closing', models.IntegerField()),
                ('loss_petrol_lit', models.IntegerField()),
                ('loss_diesel_lit', models.IntegerField()),
                ('loss_petrol_price', models.IntegerField()),
                ('loss_diesel_price', models.IntegerField()),
            ],
        ),
    ]
