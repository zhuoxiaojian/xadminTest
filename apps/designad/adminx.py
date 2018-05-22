import time

from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver

__author__ = 'cwd'
__date__ = '2018/2/25 14:19'


import os
from random import Random

from xadmin.layout import Main, Fieldset, Row, Side
import xadmin
import json
from users.models import UserProfile
from .models import DesignAdList, UserAdFileLibrary, AdVariation, SitesData, AdGoals, DesignAdSite, AdUrl, AdCreative
from django.utils.translation import ugettext as _
from utils.HttpUtils import HttpUtils
from utils.Constants import Constants
from users.tasks import postOrUpdateAdData, postOrUpdateSites


class AdCreativeInline(object):
    model = AdCreative
    exclude = ['id', 'user', 'status', 'created_at', 'varId', 'name', 'adCampaigns', 'description', 'url']
    extra = 0


class AdUrlInline(object):
    model = AdUrl
    exclude = ['id', 'user', 'created_at', 'adCampaigns', 'varId']
    extra = 0


class DesignAdAdmin(object):
    list_display = ('adName', 'adUser', 'adStyle', 'priceModel', 'price', 'maxDailyBudget', 'change_status', 'change_button')
    list_filter = ('adName', 'created_at')
    list_per_page = 20
    show_bookmarks = False #屏蔽书签
    search_fields = ['adName']
    show_detail_fields = ['adName'] #显示数据详情
    ordering = ('-created_at',)
    readonly_fields = ['addAllSite']
    refresh_times = (3, 5, 7, 10) #每5秒或7秒刷新
    # list_editable = ('priceModel', 'price', 'maxDailyBudget')  # 可编辑
    exclude = ['adUser', 'created_at', 'status', 'id', 'variation_id', 'campaign_id', 'keywords', 'isPost', 'checked'] # 不显示列
    model_icon = 'fa fa-pencil-square-o'  # 修改图标
    filter_horizontal = (
        'geographicLocationList', 'languagesList', 'mondayList', 'categoriesList',
        'tuesdayList', 'wednesdayList', 'thursdayList', 'fridayList', 'saturdayList', 'sundayList'
    )
    style_fields = {'geographicLocationList': 'm2m_transfer', 'categoriesList': 'm2m_transfer', 'languagesList': 'm2m_transfer',
                    'browsersList': 'm2m_transfer', 'operatingSystemList': 'm2m_transfer', 'mobileCarriersList': 'm2m_transfer', 'devicesList': 'm2m_transfer',
                    'mondayList': 'm2m_transfer', 'tuesdayList': 'm2m_transfer', 'wednesdayList': 'm2m_transfer',
                    'thursdayList': 'm2m_transfer', 'fridayList': 'm2m_transfer', 'saturdayList': 'm2m_transfer',
                    'sundayList': 'm2m_transfer'
                    }
    inlines = [AdUrlInline, AdCreativeInline]

    # 修改布局
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('推广内容'),
                             'adName', 'adStyle', 'categoriesList',
                             ),
                    Fieldset(_('更多选项'),
                              'sites',
                             ),
                    Fieldset(_('推广地域'),
                             'geographicLocationList',
                             ),
                    Fieldset(_('高级选项'),
                             'adAllLanguages', 'languagesList', 'adAllBrowsers', 'browsersList', 'adAllOperatingSystem', 'operatingSystemList', 'adAllMobileCarriers', 'mobileCarriersList', 'adAllDevices', 'devicesList',
                             ),
                    Fieldset(_('推广类型'),
                             Row('priceModel', 'price',),
                             'isMaxDailyBudget', 'maxDailyBudget'
                             ),
                    Fieldset(_('推广配置'),
                             Row('impressionsEnabled', 'impressions', ),
                             Row('minutes', ),
                             ),
                    Fieldset(_('站点投放'),
                             'addAllSite',
                             ),
                    Fieldset(_('推广时段'),
                             'adAllTime', 'mondayList', 'tuesdayList', 'wednesdayList', 'thursdayList', 'fridayList', 'saturdayList', 'sundayList',
                             ),
                ),
                Side(

                )
            )
        return super(DesignAdAdmin, self).get_form_layout()

    def queryset(self):
        qs = super(DesignAdAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            return qs.filter(adUser=myUser)

    def save_models(self):
        obj = self.new_obj
        obj.adUser_id = self.user.id
        obj.save()

        if obj.campaign_id != 1:
            print('PUT')
            postOrUpdateAdData.delay('PUT', obj.id, obj.adUser_id)

        else:
            print('POST')
            # 调用新建广告异步任务
            postOrUpdateAdData.delay('POST', obj.id, obj.adUser_id)


    @receiver(pre_delete, sender=DesignAdList)
    def ad_delte(sender, instance, **kwargs):
        print('删除')
        print(instance.campaign_id)
        isDel = HttpUtils.putHttp(Constants.CAMPAIGNS_DELETE_URL, {"campaign_ids": [instance.campaign_id]}, DesignAdList.objects.filter(campaign_id=instance.campaign_id)[0].adUser_id)
        if not isDel is None:
            if isDel.status_code == 200:
                print('删除成功！！！')
        pass


class UserAdFileLibraryAdmin(object):
    list_display = ('file_name', 'file_id', 'vari_file', 'type', 'width', 'height', 'file_extension', 'file_size')
    list_filter = ('type', 'file_extension', 'created_at')
    list_per_page = 20
    model_icon = 'fa fa-bell-o'
    show_bookmarks = False  # 屏蔽书签
    exclude = ['user', 'file_id', 'id', 'type', 'width', 'height', 'file_extension', 'file_size', 'url', 'localUrl', 'created_at'] # 不显示列
    ordering = ['created_at']
    show_detail_fields = ['file_name']  # 显示数据详情
    search_fields = ['user__username', 'file_name', 'type', 'file_extension']

    def queryset(self):
        qs = super(UserAdFileLibraryAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            return qs.filter(user=myUser)

    def save_models(self):
        obj = self.new_obj
        obj.user_id = self.user.id
        obj.save()

        # 上传文件则添加或更新
        if (obj.adMaterial.url).find('/designad') >= 0:
            filePath = (os.path.dirname(os.path.abspath(__file__))) \
                .replace('\\', '/') \
                .replace('/apps/designad', obj.adMaterial.url)
            print(filePath)
            fileIo = open(filePath, 'rb')
            files = {
                'file': (obj.adMaterial.url.split('/')[5], fileIo, 'multipart/form-data'),
            }
            res = HttpUtils.postHttp(Constants.IMAGE_LIBRARY_URL, files, True, obj.user_id)
            print(res)
            print(res.text)
            # 需要判断请求状态
            if not res is None:
                if res.status_code == 200:
                    print(res.text)
                    res = res.text.replace("'", '"')
                    fileInfo = json.loads(res)
                    print(fileInfo.get('url'))
                    # 关闭文件
                    fileIo.close()
                    # 删除上传的原始图片
                    # os.remove(filePath)


                    # 保存用户广告素材
                    obj.file_id = fileInfo.get('id')
                    obj.type = fileInfo.get('type')
                    obj.url = fileInfo.get('url')
                    obj.localUrl = filePath
                    obj.width = fileInfo.get('width')
                    obj.height = fileInfo.get('height')
                    obj.file_extension = fileInfo.get('file_extension')
                    obj.height = fileInfo.get('height')
                    obj.file_size = fileInfo.get('file_size_public')
                    obj.save()

                elif res.status_code == 500:
                    print(obj.adMaterial.url)
                    obj.type = '上传失败'
                    obj.save()
        pass

class AdVariationAdmin(object):
    list_display = ('name', 'adCampaigns', 'url', 'id_library_file', 'vari_file', 'change_status', 'change_button')
    list_filter = ('name', 'adCampaigns')
    search_fields = ['user__username', 'name', 'adCampaigns__adName', 'url', 'id_library_file']
    list_per_page = 20
    show_bookmarks = False  # 屏蔽书签
    model_icon = 'fa fa-file-word-o'
    show_detail_fields = ['name']  # 显示数据详情
    exclude = ['id', 'user', 'status', 'varId', 'description', 'vari_url']  # 不显示列

    def save_models(self):
        obj = self.new_obj
        obj.save()

    def queryset(self):
        qs = super(AdVariationAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            return qs.filter(user=myUser)

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False


class SitesDataAdmin(object):
    list_display = ('site_hostname', 'adCampaigns',  'ctr', 'cost', 'impressions', 'clicks', 'avgCpc', 'avgCpm', 'G1', 'ecpa1', 'G2', 'ecpa2', 'G3', 'ecpa3', 'G4', 'ecpa4')
    list_filter = ('site_hostname', 'cost', 'impressions', 'clicks', 'avgCpc', 'avgCpm', 'date')
    search_fields = ['user__username', 'site_hostname', 'adCampaigns__adName']
    list_per_page = 30
    model_icon = 'fa fa-table'
    ordering = ['-cost', '-impressions', 'clicks', 'avgCpc', 'avgCpm', 'G1', 'ecpa1', 'G2', 'ecpa2', 'G3', 'ecpa3', 'G4', 'ecpa4']
    show_bookmarks = False  # 屏蔽书签
    show_detail_fields = ['site_hostname']  # 显示数据详情
    exclude = []  # 不显示列
    import_excel = True
    # 求总和
    aggregate_fields = {'ctr': 'sum', 'cost': 'sum', 'impressions': 'sum', 'clicks': 'sum', 'avgCpc': 'avg', 'avgCpm': 'avg', 'G1': 'sum', 'ecpa1': 'avg', 'G2': 'sum', 'ecpa2': 'avg', 'G3': 'sum', 'ecpa3': 'avg', 'G4': 'sum', 'ecpa4': 'avg'}

    def queryset(self):
        if self.user.is_superuser:
            return super(SitesDataAdmin, self).queryset()
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            qs = SitesData.objects.filter(user=myUser)
            return qs.extra(select={
                'ctr': "CONCAT(FORMAT(ctr, 2), '%%')",
                'cost': 'CONVERT(cost / deliveryRate, DECIMAL(10,2))',
                'avgCpc': 'CONVERT(avgCpc / deliveryRate, DECIMAL(10,2))',
                'avgCpm': 'CONVERT(avgCpm / deliveryRate, DECIMAL(10,2))',
                'ecpa1': 'CONVERT(ecpa1 / deliveryRate, DECIMAL(10,2))',
                'ecpa2': 'CONVERT(ecpa2 / deliveryRate, DECIMAL(10,2))',
                'ecpa3': 'CONVERT(ecpa3 / deliveryRate, DECIMAL(10,2))',
                'ecpa4': 'CONVERT(ecpa4 / deliveryRate, DECIMAL(10,2))',
            })

    # 屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
            return False


class AdGoalsAdmin(object):
    list_display = ('name',  'order', 'coa',  'goalScript')
    list_filter = ('name',  'order', 'coa', 'goalScript')
    search_fields = ['user__username', 'name', 'order', 'coa', 'goalScript']
    # list_editable = ('goalScript')
    list_per_page = 20
    model_icon = 'fa fa-hand-o-up'
    show_bookmarks = False  # 屏蔽书签
    show_detail_fields = ['name']  # 显示数据详情
    ordering = ['order']
    exclude = ['user', 'goalId', 'idUser', 'seq', 'goalScript']  # 不显示列

    def save_models(self):

        obj = self.new_obj
        obj.user_id = self.user.id
        obj.save()
        name = obj.name
        order = obj.order
        coa = obj.coa
        # adGoals = AdGoals.objects.filter(name=AdGoals.objects.get(id=obj.id).name).count()
        if obj.goalId != '0':
            postOrUpdateGoal = HttpUtils.putHttp(Constants.GOALS_UPDATE_OR_DELETE_URL.format(AdGoals.objects.get(name=name).goalId), getPostGoals(name, order, coa), obj.user_id)
            if postOrUpdateGoal.status_code == 200:
                obj.goalScript = '<!-- START MonAdvert  Goal Tag | ' + name + ' --><script type="text/javascript" src="http://service.monadvert.com/tag_gen.js" data-goal="' + obj.goalId + '"></script><!-- END MonAdvert  Goal Tag | ' + name + ' -->'
                AdGoals.objects.filter(name=name).update(goalId=obj.goalId,
                                                         goalScript=obj.goalScript)
        elif obj.goalId == '0':
            postOrUpdateGoal = HttpUtils.postHttp(Constants.GOALS_URL, getPostGoals(name, order, coa), False,
                                                  obj.user_id)
            if postOrUpdateGoal.status_code == 200:
                obj.goalId = postOrUpdateGoal.text.split(':')[1].split('}')[0].strip("\"")
                obj.goalScript = '<!-- START MonAdvert  Goal Tag | ' + name + ' --><script type="text/javascript" src="http://service.monadvert.com/tag_gen.js" data-goal="' + obj.goalId + '"></script><!-- END MonAdvert  Goal Tag | ' + name + ' -->'

                AdGoals.objects.filter(name=name).update(goalId=obj.goalId,
                                                          goalScript=obj.goalScript)


    @receiver(pre_delete, sender=AdGoals)
    def ad_delte(sender, instance, **kwargs):
        print('删除')
        print(instance.goalId)
        isDel = HttpUtils.deleteHttp(Constants.GOALS_UPDATE_OR_DELETE_URL.format(instance.goalId),
                                     instance.user_id)
        if not isDel is None:
            if isDel.status_code == 200:
                print('删除成功！！！')
        pass


    def queryset(self):
        qs = super(AdGoalsAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            return qs.filter(user=myUser)


class DesignAdSiteAdmin(object):
    list_display = ('adName', 'sites')
    list_filter = ('adName', 'sites')
    search_fields = ['adName', 'sites']
    list_per_page = 20
    model_icon = 'fa fa-paper-plane-o'
    show_bookmarks = False  # 屏蔽书签
    exclude = ['adUser', 'adName', 'adStyle', 'keywords',  'maxDailyBudget', 'addAllSite', 'categoriesList', 'languagesList', 'browsersList', 'operatingSystemList', 'mobileCarriersList', 'devicesList', 'priceModel', 'price', 'geographicLocationList', 'languagesList', 'mondayList', 'categoriesList',
        'tuesdayList', 'wednesdayList', 'thursdayList', 'fridayList', 'saturdayList', 'sundayList', 'adAllTime', 'campaign_id', 'status', 'variation_id', 'created_at', 'isPost']

    def queryset(self):
        qs = super(DesignAdSiteAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            myUser = UserProfile.objects.get(id=self.user.id)
            return qs.filter(adUser=myUser)

    def save_models(self):
        obj = self.new_obj
        obj.adUser_id = self.user.id
        obj.save()

        print('PUT')
        postOrUpdateSites.delay('PUT', obj.campaign_id, obj.sites, obj.adUser_id)

    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False


xadmin.site.register(DesignAdList, DesignAdAdmin)
xadmin.site.register(UserAdFileLibrary, UserAdFileLibraryAdmin)
xadmin.site.register(AdVariation, AdVariationAdmin)
xadmin.site.register(DesignAdSite, DesignAdSiteAdmin)
xadmin.site.register(SitesData, SitesDataAdmin)
xadmin.site.register(AdGoals, AdGoalsAdmin)



def getPostGoals(name,order,coa):
    if not coa is None:
        postGoalJson = {
            'name':name,
            'order':order,
            # 'coa':coa
        }
        return postGoalJson
    else:
        postGoalJson = {
            'name': name,
            'order': order,
        }
        return postGoalJson