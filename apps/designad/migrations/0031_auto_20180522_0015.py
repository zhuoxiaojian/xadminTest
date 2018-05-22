# Generated by Django 2.0.4 on 2018-05-22 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0030_auto_20180520_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designadlist',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.10', help_text='CPC模式的价格不能超过1.66', max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='价格'),
        ),
    ]
