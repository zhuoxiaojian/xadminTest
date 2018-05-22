from django.db import models
from datetime import datetime

from users.models import UserProfile
from designad.models import DesignAdList


# Create your models here.
class CostDailyReport(models.Model):
    adUser = models.ForeignKey(UserProfile, verbose_name='用户', null=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name='消费', default='0.00', null=True, db_index=True)
    impressions = models.IntegerField(verbose_name='展现次数', default='0', null=True)
    clicks = models.IntegerField(verbose_name='点击次数', default='0', null=True)
    avgCpc = models.FloatField(verbose_name='Avg_CPC', default='0.00', null=True, db_index=True)
    ctr = models.FloatField(verbose_name='点击率', default='0.00', null=True)
    deliveryRate = models.FloatField(verbose_name='投放率', max_length=50, default='0.00', null=True, db_index=True)
    date = models.DateField(verbose_name='消费时间', default=datetime.now, null=True)

    class Meta:
        verbose_name = '消费日统计报表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adUser.username

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False


class CostHourReport(models.Model):
    adUser = models.ForeignKey(UserProfile, verbose_name='用户', null=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name='消费',  default='0.00', null=True, db_index=True)
    impressions = models.IntegerField(verbose_name='展现次数',  default='0', null=True)
    clicks = models.IntegerField(verbose_name='点击次数', default='0', null=True)
    avgCpc = models.FloatField(verbose_name='Avg_CPC',  default='0.00', null=True, db_index=True)
    ctr = models.FloatField(verbose_name='点击率', default='0.00', null=True)
    deliveryRate = models.FloatField(verbose_name='投放率', max_length=50, default='0.00', null=True, db_index=True)
    date = models.DateTimeField(verbose_name='消费时间（纽约时间）', default=datetime.now, null=True)

    class Meta:
        verbose_name = '消费时统计报表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adUser.username

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

