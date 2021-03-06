# Generated by Django 2.0.4 on 2018-05-17 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0025_auto_20180517_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designadlist',
            name='maxDailyBudget',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(100)], verbose_name='日均预算上限'),
        ),
    ]
