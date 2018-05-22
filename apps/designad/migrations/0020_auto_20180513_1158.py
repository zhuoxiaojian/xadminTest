# Generated by Django 2.0.4 on 2018-05-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0019_auto_20180511_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='designadlist',
            name='adAllBrowsers',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下浏览器不用再选择', verbose_name='选择全部浏览器'),
        ),
        migrations.AddField(
            model_name='designadlist',
            name='adAllDevices',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下设备不用再选择', verbose_name='选择全部设备'),
        ),
        migrations.AddField(
            model_name='designadlist',
            name='adAllLanguages',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下语言不用再选择', verbose_name='选择全部语言'),
        ),
        migrations.AddField(
            model_name='designadlist',
            name='adAllMobileCarriers',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下移动运营商不用再选择', verbose_name='选择全部移动运营商'),
        ),
        migrations.AddField(
            model_name='designadlist',
            name='adAllOperatingSystem',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下操作系统不用再选择', verbose_name='选择全部操作系统'),
        ),
    ]