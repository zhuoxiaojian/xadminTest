# Generated by Django 2.0.4 on 2018-05-11 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0018_auto_20180511_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designadlist',
            name='adAllBrowsers',
        ),
        migrations.RemoveField(
            model_name='designadlist',
            name='adAllDevices',
        ),
        migrations.RemoveField(
            model_name='designadlist',
            name='adAllLanguages',
        ),
        migrations.RemoveField(
            model_name='designadlist',
            name='adAllMobileCarriers',
        ),
        migrations.RemoveField(
            model_name='designadlist',
            name='adAllOperatingSystem',
        ),
    ]
