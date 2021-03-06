# Generated by Django 2.0.4 on 2018-05-19 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0028_auto_20180517_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designadlist',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.10', help_text='最低出价是0.20，其中CPC模式的价格不能超过11.60', max_digits=10, validators=[django.core.validators.MaxValueValidator(11.6), django.core.validators.MinValueValidator(0.2)], verbose_name='价格'),
        ),
    ]
