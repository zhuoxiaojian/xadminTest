# Generated by Django 2.0.4 on 2018-05-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0008_auto_20180418_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designadlist',
            options={'verbose_name': '广告活动', 'verbose_name_plural': '广告活动'},
        ),
        migrations.AlterField(
            model_name='sitesdata',
            name='avgCpc',
            field=models.FloatField(db_index=True, default='0.00', null=True, verbose_name='Avg_CPC'),
        ),
        migrations.AlterField(
            model_name='sitesdata',
            name='avgCpm',
            field=models.FloatField(db_index=True, default='0.00', null=True, verbose_name='Avg_CPM'),
        ),
        migrations.AlterField(
            model_name='useradfilelibrary',
            name='file_id',
            field=models.BigIntegerField(default='1', verbose_name='创意id'),
        ),
        migrations.AlterField(
            model_name='useradfilelibrary',
            name='file_name',
            field=models.CharField(default='', max_length=250, verbose_name='创意名称'),
        ),
    ]
