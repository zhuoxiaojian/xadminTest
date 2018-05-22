from django.contrib import admin
import xadmin

from .models import MinimumPrices


# Register your models here.
class MinimumPricesAdmin(object):
    list_display = (
        'format',
        'geo',
        'category',
        'network_selection_type',
        'web_cpc',
        'mobile_cpc',
        'web_cpm',
        'mobile_cpm'
    )
    list_filter = (
        'format',
        'geo',
        'category',
        'web_cpc',
        'mobile_cpc',
        'web_cpm',
        'mobile_cpm'
    )
    search_fields = [
        'format',
        'geo',
        'category',
        'web_cpc',
        'mobile_cpc',
        'web_cpm',
        'mobile_cpm'
    ]
    list_per_page = 20
    ordering = (
        'format',
        'geo',
        'category',
        'web_cpc',
        'mobile_cpc',
        'web_cpm',
        'mobile_cpm'
    )
    model_icon = 'fa fa-book'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
    refresh_times = (3, 5, 7, 10)  # 每5秒或7秒刷新

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False


xadmin.site.register(MinimumPrices, MinimumPricesAdmin)
