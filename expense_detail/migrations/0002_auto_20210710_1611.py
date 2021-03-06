# Generated by Django 3.2.4 on 2021-07-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='electricity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='employee_insurance_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='insurence_expence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='labour_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='machinory_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='maintainence_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='property_tax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='remark',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='ruff_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='stationary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='tea_coffee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='total_Amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='water_bill',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
