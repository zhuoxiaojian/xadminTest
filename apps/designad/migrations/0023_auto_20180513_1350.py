# Generated by Django 2.0.4 on 2018-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0022_auto_20180513_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designadlist',
            name='adAllLanguages',
            field=models.BooleanField(default=False, help_text='提示：选择了此处，则以下语言不用再选择', verbose_name='选择全部语言'),
        ),
    ]