# Generated by Django 2.0.4 on 2018-05-17 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0024_auto_20180513_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='designadlist',
            name='isMaxDailyBudget',
            field=models.BooleanField(default=True, help_text='提示：选择了此处，下面设置的日均预算上限数值才会生效。若不选择此处则日均预算上限默认是无限', verbose_name='设置日均预算上限'),
        ),
        migrations.AlterField(
            model_name='designadlist',
            name='maxDailyBudget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(100)], verbose_name='日均预算上限'),
        ),
    ]
