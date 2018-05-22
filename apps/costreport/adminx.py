import xadmin
from designad.models import DesignAdList
from xadmin.views import filter_hook
from .models import CostDailyReport, CostHourReport
from users.models import UserProfile


# Register your models here.
class CostDailyReportAdmin(object):
    list_display = (
        'adCampaigns',
        'cost',
        'impressions',
        'clicks',
        'avgCpc',
        'ctr',
        'adUser',
        'date'
    )
    list_filter = (
        'date',
    )
    search_fields = [
        'adUser__username',
        'adCampaigns__adName',
    ]
    show_detail_fields = ['adCampaigns']
    list_per_page = 20
    ordering = (
        '-cost',
        '-impressions',
        'clicks',
        'avgCpc',
        'ctr',
        'date',
    )
    readonly_fields = (
        'cost',
        'impressions',
        'clicks',
        'avgCpc',
        'ctr',
        'date',
    )
    exclude = [
        'adCampaigns',
        'adUser',
        'deliveryRate'
    ]
    model_icon = 'fa fa-list-alt'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
    refresh_times = (3, 5, 7, 10)  # 每5秒或7秒刷新
    # 求总和
    aggregate_fields = {'cost': 'sum', 'impressions': 'sum', 'clicks': 'sum', 'avgCpc': 'avg', 'ctr': 'sum'}

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def queryset(self):
        if self.user.is_superuser:
            return super(CostDailyReportAdmin, self).queryset()
        else:
            qs = CostDailyReport.objects.filter(adUser_id=self.user.id).extra(select={
                'ctr': "CONCAT(FORMAT(ctr, 2), '%%')",
                'cost': 'CONVERT(cost / deliveryRate, DECIMAL(10,2))',
                'avgCpc': 'CONVERT(avgCpc / deliveryRate, DECIMAL(10,2))',
            })
            return qs

    # @filter_hook
    # def get_model_form(self, **kwargs):
    #     form = super(CostDailyReportAdmin, self).get_model_form(**kwargs)
    #     form.base_fields['adCampaigns'].queryset = DesignAdList.objects.filter(adUser_id=self.user.id)
    #     return form


class CostHourReportAdmin(object):
    list_display = (
        'adCampaigns',

        'cost',
        'impressions',
        'clicks',
        'avgCpc',
        'ctr',
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
    list_per_page = 20
    ordering = (
        '-cost',
        '-impressions',
        'clicks',
        'avgCpc',
        'ctr',
        'date',
    )
    readonly_fields = (
        'cost',
        'impressions',
        'clicks',
        'avgCpc',
        'ctr',
        'date',
    )
    exclude = [
        'adCampaigns',
        'adUser',
        'deliveryRate'
    ]
    show_detail_fields = ['adCampaigns']
    model_icon = 'fa fa-file-text-o'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
    refresh_times = (3, 5, 7, 10)  # 每3秒或5秒刷新
    # 求总和
    aggregate_fields = {'cost': 'sum', 'impressions': 'sum', 'clicks': 'sum', 'avgCpc': 'avg', 'ctr': 'sum'}

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    def queryset(self):
        if self.user.is_superuser:
            return super(CostHourReportAdmin, self).queryset()
        else:
            qs = CostHourReport.objects.filter(adUser_id=self.user.id).extra(select={
                'ctr': "CONCAT(FORMAT(ctr, 2), '%%')",
                'cost': 'CONVERT(cost / deliveryRate, DECIMAL(10,2))',
                'avgCpc': 'CONVERT(avgCpc / deliveryRate, DECIMAL(10,2))',
            })
            return qs


xadmin.site.register(CostDailyReport, CostDailyReportAdmin)
xadmin.site.register(CostHourReport, CostHourReportAdmin)
