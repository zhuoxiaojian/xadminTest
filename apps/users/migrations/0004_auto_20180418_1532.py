# Generated by Django 2.0.4 on 2018-04-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180416_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracount',
            name='dailyCost',
            field=models.FloatField(default=0.0, null=True, verbose_name='今日消费金额'),
        ),
        migrations.AlterField(
            model_name='useracount',
            name='deliveryRate',
            field=models.FloatField(default=0.0, max_length=50, null=True, verbose_name='投放率'),
        ),
        migrations.AlterField(
            model_name='useracount',
            name='exchangeRate',
            field=models.FloatField(default=0.0, max_length=50, null=True, verbose_name='汇率'),
        ),
        migrations.AlterField(
            model_name='useracount',
            name='monthCost',
            field=models.FloatField(default=0.0, null=True, verbose_name='本月消费金额'),
        ),
    ]
