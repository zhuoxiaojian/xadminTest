from django.contrib import admin
# Register your models here.
import xadmin
from .models import CostDailyTrendReport,CostHourTrendReport
from users.models import UserProfile


class CostDailyTrendReportAdmin(object):
    list_display = (
        'adCampaigns',
        'cost',
        'adUser',
        'date',
    )
    list_filter = (
        'date',
    )
    search_fields = [
        'adUser__username',
        'adCampaigns__adName',
    ]
    readonly_fields = (
        'adUser',
        'adCampaigns',
        'cost',
        'date',
    )
    exclude = [
        'adUser',
        'adCampaigns',
        'deliveryRate'
    ]
    model_icon = 'fa fa-line-chart'  # 修改图标
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    show_detail_fields = ['adCampaigns']  # 显示数据详情
    refresh_times = (3, 5, 7, 10)  # 每5秒或7秒刷新
    # 求总和
    aggregate_fields = {'cost': 'sum'}

    data_charts = {
        "user_count": {'title': "消费趋势报表", "x-field": "date", "y-field": ("cost",),
                       "order": ('date',)},
    }


    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def queryset(self):
        if self.user.is_superuser:
            return super(CostDailyTrendReportAdmin, self).queryset()
        else:
            qs = CostDailyTrendReport.objects.filter(adUser_id=self.user.id)
            return qs


class CostHourTrendReportAdmin(object):
    list_display = (
        'adCampaigns',
        'cost',
        'adUser',
        'date',
    )
    list_filter = (
        'date',
    )
    search_fields = [
        'adUser__username',
        'adCampaigns__adName',
    ]
    readonly_fields = (
        'adUser',
        'adCampaigns',
        'cost',
        'date',
    )
    exclude = [
        'adUser',
        'adCampaigns',
        'deliveryRate'
    ]
    model_icon = 'fa fa-bar-chart'  # 修改图标
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    show_detail_fields = ['adCampaigns']  # 显示数据详情
    refresh_times = (3, 5, 7, 10)  # 每3秒或5秒刷新
    aggregate_fields = {'cost': 'sum'}

    data_charts = {
        "user_count": {'title': "消费趋势报表", "x-field": "date", "y-field": ("cost",),
                       "order": ('date',)},
    }


    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def queryset(self):
        if self.user.is_superuser:
            return super(CostHourTrendReportAdmin, self).queryset()
        else:
            qs = CostHourTrendReport.objects.filter(adUser_id=self.user.id)
            return qs


xadmin.site.register(CostDailyTrendReport, CostDailyTrendReportAdmin)
xadmin.site.register(CostHourTrendReport, CostHourTrendReportAdmin)