# Generated by Django 2.0.4 on 2018-05-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_useracount_recharge_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='useracount',
            name='recharge_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='本次充值时EXO的余额'),
        ),
    ]
