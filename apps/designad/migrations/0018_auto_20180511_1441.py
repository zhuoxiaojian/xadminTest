# Generated by Django 2.0.4 on 2018-05-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0017_auto_20180511_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='designadlist',
            name='adAllOperatingSystem',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下操作系统不用再选择', verbose_name='选择全部操作系统'),
        ),
        migrations.AlterField(
            model_name='designadlist',
            name='adAllBrowsers',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下浏览器不用再选择', verbose_name='选择全部浏览器'),
        ),
    ]
