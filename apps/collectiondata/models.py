from django.db import models

# Create your models here.
class MinimumPrices(models.Model):
    format = models.CharField(verbose_name='广告材料格式', max_length=30, default='BANNERS')
    geo = models.CharField(verbose_name='地理位置', max_length=100, default='CHN')
    category = models.CharField(verbose_name='类别', max_length=10, default='2')
    network_selection_type = models.CharField(verbose_name='网络选择类型', max_length=50, default='0')
    web_cpc = models.CharField(verbose_name='web cpc', max_length=10, default='0.01')
    mobile_cpc = models.CharField(verbose_name='mobile cpc', max_length=10, default='0.01')
    web_cpm = models.CharField(verbose_name='web cpm', max_length=10, default='0.01')
    mobile_cpm = models.CharField(verbose_name='mobile cpm', max_length=10, default='0.01')

    class Meta:
        verbose_name = '广告最低价格表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.geo