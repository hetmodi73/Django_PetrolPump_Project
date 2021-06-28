# Generated by Django 3.2.4 on 2021-06-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creditors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('office_no', models.IntegerField()),
                ('contact_person_name', models.CharField(max_length=20)),
                ('contact_person_mobile_no', models.IntegerField()),
                ('company_name', models.CharField(max_length=20)),
                ('home_no', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=20)),
                ('area_name', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('gst_no', models.IntegerField()),
                ('pending_balance', models.IntegerField()),
                ('creation_date', models.IntegerField()),
            ],
        ),
    ]