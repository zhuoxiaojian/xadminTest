# Generated by Django 2.0.4 on 2018-05-09 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rechargerecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adpricerate',
            name='exchangeRate',
        ),
        migrations.RemoveField(
            model_name='useracount',
            name='exchangeRate',
        ),
    ]