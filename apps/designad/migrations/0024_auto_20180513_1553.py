# Generated by Django 2.0.4 on 2018-05-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designad', '0023_auto_20180513_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesdata',
            name='adCampaigns',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='designad.DesignAdList', verbose_name='所属广告活动'),
        ),
    ]
