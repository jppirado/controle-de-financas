# Generated by Django 4.2.1 on 2023-05-16 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da Compra')),
                ('value', models.FloatField()),
                ('date', models.DateField(default=datetime.datetime(2023, 5, 15, 22, 15, 9, 650001), verbose_name='Data da compra')),
            ],
        ),
    ]
