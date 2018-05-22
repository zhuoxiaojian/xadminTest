from django.db import models
from datetime import datetime
from users.models import UserProfile
from designad.models import DesignAdList


# Create your models here.
class CostDailyTrendReport(models.Model):
    adUser = models.ForeignKey(UserProfile, verbose_name='用户', null=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name='消费', default='0.00', null=True, db_index=True)
    deliveryRate = models.FloatField(verbose_name='投放率', max_length=50, default='0.00', null=True, db_index=True)
    date = models.DateField(verbose_name='消费日期', default=datetime.now, null=True)

    class Meta:
        verbose_name = '消费日趋势报表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adUser.username


class CostHourTrendReport(models.Model):
    adUser = models.ForeignKey(UserProfile, verbose_name='用户', null=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name='消费', default='0.00', null=True, db_index=True)
    deliveryRate = models.FloatField(verbose_name='投放率', max_length=50, default='0.00', null=True, db_index=True)
    date = models.DateTimeField(verbose_name='消费日期（纽约时间）', default=datetime.now, null=True)

    class Meta:
        verbose_name = '消费时趋势报表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adUser.username
