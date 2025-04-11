# Generated by Django 5.0.6 on 2025-03-30 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0006_alter_items_item_name_alter_items_low_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=50)),
                ('Entry_no', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('tota_qty', models.IntegerField()),
                ('total_amount', models.BigIntegerField()),
                ('paid_amount', models.BigIntegerField()),
                ('due_amount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='purchase_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('purchase_price', models.BigIntegerField()),
                ('amount', models.BigIntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.purchase_bill')),
            ],
        ),
    ]
