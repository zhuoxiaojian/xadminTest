# Generated by Django 2.0.4 on 2018-04-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0004_auto_20180417_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='geographiclocation',
            name='long_name',
            field=models.CharField(default='China', max_length=250, verbose_name='地理位置简称'),
        ),
    ]