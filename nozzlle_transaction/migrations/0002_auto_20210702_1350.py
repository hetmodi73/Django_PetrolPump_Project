# Generated by Django 3.2.4 on 2021-07-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nozzlle_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nozzlle_t',
            name='credit_debit_card',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='Opening_lit_Diesel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='cash',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='closing_lit_Diesel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='closing_lit_petrol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='googlePay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='loss_price_diesel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='loss_price_petrol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='opening_lit_petrol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='paytm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='phonePay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_lit_diesel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_lit_petrol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_price_diesel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='total_price_petrol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlle_t',
            name='upi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
