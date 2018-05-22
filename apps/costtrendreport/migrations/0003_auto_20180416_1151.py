# Generated by Django 2.0.4 on 2018-04-16 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('costtrendreport', '0002_costhourtrendreport_adcampaigns'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costhourtrendreport',
            name='adUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='costdailytrendreport',
            name='adCampaigns',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='designad.DesignAdList', verbose_name='所属广告活动'),
        ),
        migrations.AddField(
            model_name='costdailytrendreport',
            name='adUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
