import json
import time

from users.models import AdPriceRate, UserAcount, RechargeRecord
from users.tasks import updateSitesDataRate
from utils.Constants import Constants
from utils.HttpUtils import HttpUtils

__author__ = 'cwd'
__date__ = '2018/2/27 10:04'

from xadmin import views
import xadmin


class BaseSetting(object):
    # 主题切换
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    # 系统标题
    site_title = 'MonAdert'
    # 底部栏
    site_footer = 'Copyright 2018, MonAdert.'

    menu_style = 'accordion'


class AdPriceRateAdmin(object):
    list_display = ('user', 'deliveryRate', 'created_time')
    list_filter = ('user', 'deliveryRate', 'created_time')
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    search_fields = ['user__username', 'deliveryRate']
    show_detail_fields = ['user']  # 显示数据详情
    ordering = ('-created_time',)
    # exclude = ['user',]
    #exclude = ['created_time']  # 不显示列
    model_icon = 'fa fa-dollar'  # 修改图标

    def save_models(self):
        obj = self.new_obj
        # obj.save()
        # 获取最新的余额
        resp = HttpUtils.getHttp(Constants.USER_ACOUNT_URL, obj.user.id)
        if not resp is None:
            if resp.status_code == 200:
                body = json.loads(resp.text)
                result = body.get('result')
                if float(result.get('balance')) < 0:
                    UserAcount.objects.filter(user_id=obj.user.id).update(recharge_balance=result.get('balance'))

        obj.save()
        # 动态调整
        updateSitesDataRate.delay(obj.user.id)


class UserAcountAdmin(object):
    list_display = ('user', 'balance', 'dailyCost', 'monthCost')
    # list_filter = ('user', 'balance', 'dailyCost', 'monthCost')
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    # search_fields = ['user__username',]
    show_detail_fields = ['user']  # 显示数据详情
    ordering = ('-balance',)
    exclude = ['recharge_balance']  # 不显示列
    model_icon = 'fa fa-university'  # 修改图标

    def queryset(self):
        qs = super(UserAcountAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            qs = UserAcount.objects.filter(user_id=self.user.id).extra(select={
                'balance': 'CONVERT(balance, DECIMAL(10,2))',
                'dailyCost': 'CONVERT(dailyCost, DECIMAL(10,2))',
                'monthCost': 'CONVERT(monthCost, DECIMAL(10,2))',
            })
            return qs

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False


class RechargeRecordAdmin(object):
    list_display = ('user', 'recharge', 'exo_recharge', 'created_time')
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    search_fields = ['user__username',]
    show_detail_fields = ['user']  # 显示数据详情
    exclude = ['recharge_deliveryRate']
    ordering = ('-created_time',)
    model_icon = 'fa fa-credit-card'  # 修改图标

    def save_models(self):
        obj = self.new_obj
        deliveryRate = AdPriceRate.objects.filter(user_id=obj.user.id).order_by('-created_time')[0].deliveryRate
        obj.recharge_deliveryRate = deliveryRate
        obj.save()




xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.LoginView,
    login_template="xadmin/views/xadmin_login.html"
    )
xadmin.site.register(AdPriceRate, AdPriceRateAdmin)
xadmin.site.register(UserAcount, UserAcountAdmin)
xadmin.site.register(RechargeRecord, RechargeRecordAdmin)