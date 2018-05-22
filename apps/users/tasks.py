__author__ = 'cwd'
__date__ = '2018/3/12 10:21'

import json
import time
import datetime

from designad.models import DesignAdList, UserAdFileLibrary, AdVariation, AdUrl, AdCreative
from utils import ConversionUtils, JsonUtils
from utils.Constants import Constants
from utils.HttpUtils import HttpUtils
from utils.TokenUtils import TokenUtils
from users.models import UserProfile, UserAcount, RechargeRecord, AdPriceRate

from celery import task
from utils.InitDataUtils import InitData

# 接收上传参数
adPostOrUpdate = ''
keywordsList = ''

budget_list = [20, 50, 100,
               200, 500, 750,
               1000, 2000, 5000,
               10000, 15000, 20000
               ]
maxDailyBudget = 0

# 获取广告日消费数据
@task
def getAdData():
    print('获取用户广告消费数据定时任务开始。。。。。')
    url = Constants.CAMPAIGNS_URL
    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            print('获取用户数据ID::'+str(userId))
            n = HttpUtils.getHttp(url, userId)
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for adStatus in result:
                    print(adStatus)
                    InitData.getAdStatistics(adStatus, userId)

            print('获取用户广告消费数据定时任务睡眠5s')
            time.sleep(5)
            print('获取用户广告消费数据定时任务睡眠结束')
    print('获取用户广告消费数据定时任务结束。。。。。')
    pass


# 获取站点数据定时任务
@task
def getSitesData():
    print('获取用户站点数据定时任务开始。。。。。')
    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            print('获取用户数据ID::'+str(userId))
            InitData.getSitesData(userId)
            print('获取用户站点数据定时任务睡眠5s')
            time.sleep(5)
            print('获取用户站点数据定时任务睡眠结束')
    print('获取用户站点数据定时任务结束。。。。。')
    pass


# 获取广告时消费数据
@task
def getAdHourData():
    print('获取用户分时数据定时任务开始。。。。。')
    url = Constants.CAMPAIGNS_URL
    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            n = HttpUtils.getHttp(url, userId)
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for adStatus in result:
                    print(adStatus)
                    InitData.getHourData(adStatus, userId)

            time.sleep(5)
    print('获取用户分时数据定时任务结束。。。。')

@task
def getCamp():
    print('同步用户广告定时任务开始。。。。。')
    InitData.getAllCamp(0)
    print('同步用户广告定时任务结束。。。。。')


@task
def getGoals():
    print('获取goal定时任务开始。。。。。')
    InitData.getGoals(0)
    print('获取goal定时任务结束。。。。。')

# 刷新Token定时任务
@task
def getToken():
    print('刷新Token定时任务开始。。。。。')
    userList = UserProfile.objects.all()
    print(userList.count())
    for user in userList:
        print(user.exo_name)
        print(user.exo_password)
        TokenUtils.getAPIToken(user.exo_name, user.exo_password)
    print('刷新Token定时任务结束。。。。。')
    pass


@task
def getVariStatus():
    print('获取广告材料状态定时任务开始。。。。。')
    url = Constants.CAMPAIGNS_URL
    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            n = HttpUtils.getHttp(url, userId)
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for adVariStatus in result:
                    # print(adVariStatus)
                    InitData.getVariStatus(adVariStatus, userId)
            time.sleep(30)
    print('获取广告材料状态定时任务结束。。。。。')


@task
def getUserAcount():
    print('获取用户余额定时任务开始')

    today = datetime.date.today()
    userList = UserProfile.objects.all()
    for user in userList:
        balance = 0
        monthCost = 0
        dailyCost = 0
        pre_rate = 0
        userId = user.id

        if user.is_superuser != 1:
            rate = ConversionUtils.getRate(userId, datetime.datetime.combine(today, datetime.time()))
            deliveryRate = rate.get('deliveryRate')
            resp = HttpUtils.getHttp(Constants.USER_ACOUNT_URL, userId)
            if not resp is None:
                if resp.status_code == 200:
                    body = json.loads(resp.text)
                    result = body.get('result')
                    if not type(result) is list:
                        # 获取最新的充值记录
                        if RechargeRecord.objects.filter(user_id=userId).order_by('-created_time').exists():
                            recode = RechargeRecord.objects.filter(user_id=userId).order_by('-created_time')[0]

                            # 获取前一次充值的投放率
                            user_acount = UserAcount.objects.filter(user_id=userId)
                            if AdPriceRate.objects.filter(user_id=userId).order_by('-created_time').count() > 1:
                                pre_rate = AdPriceRate.objects.filter(user_id=userId).order_by('-created_time')[1].deliveryRate
                            # 当余额为负数或0的时候，如果不为0则需减去剩余额
                            recharge = recode.recharge
                            if pre_rate != 0 and pre_rate != recode.recharge_deliveryRate:
                                exo_recharge = (float(result.get('balance')) / float(deliveryRate)) - (float(user_acount[0].recharge_balance) / float(pre_rate))

                            else:
                                exo_recharge = (float(recode.exo_recharge) / float(deliveryRate))

                            balance = round(float(result.get('balance') / float(deliveryRate)) + float(recharge) - exo_recharge, 2)


            resp = HttpUtils.getHttp(Constants.STATISTICS_ADVERTISER_DATE_ACOUNT.format(today, today), userId)
            # print(Constants.STATISTICS_ADVERTISER_DATE_ACOUNT.format(today, today))
            if not resp is None:
                if resp.status_code == 200:
                    body = json.loads(resp.text)
                    result = body.get('result')

                    for costDailyData in result:
                        dailyCost = round(float(costDailyData.get('cost')) / float(deliveryRate), 2)
                        # print(dailyCost)
                        # 只获取第一个数据，就是今天的消费数据，可省略
                        break

            day_now = datetime.date.today()
            day_begin = '%d-%02d-01' % (day_now.year, day_now.month)

            resp = HttpUtils.getHttp(Constants.STATISTICS_ADVERTISER_DATE_ACOUNT.format(today, day_begin), userId)
            # print(Constants.STATISTICS_ADVERTISER_DATE_ACOUNT.format(today, day_begin))
            if not resp is None:
                if resp.status_code == 200:
                    body = json.loads(resp.text)
                    result = body.get('result')

                    for dailyCostData in result:
                        rate = ConversionUtils.getRate(userId, datetime.datetime.strptime(dailyCostData.get('ddate'), '%Y-%m-%d'))
                        per_day_delivery_rate = rate.get('deliveryRate')
                        monthCost += round(float(dailyCostData.get('cost') / float(per_day_delivery_rate)), 2)

                        print('{0}:::{1}'.format(round(float(dailyCostData.get('cost')), 2), monthCost))

            if UserAcount.objects.filter(user_id=userId).exists():
                UserAcount.objects.filter(user_id=userId).update(
                                                               balance=balance,
                                                               dailyCost=dailyCost,
                                                               monthCost=monthCost,
                                                               )
            elif not UserAcount.objects.filter(user_id=userId).exists():
                userAcount = UserAcount()
                userAcount.user_id = userId
                userAcount.balance = balance
                userAcount.dailyCost = dailyCost
                userAcount.monthCost = monthCost
                UserAcount.save(userAcount)
    print('获取用户余额定时任务结束')


# 检查是否有广告因为网络原因或者接口问题未上传成功并上传未上传的广告
@task
def checkAdIsPost():
    print('查询广告是否上传成功并上传未上传的广告的定时任务开始')

    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            designList = DesignAdList.objects.filter(isPost=0, adUser_id=userId)
            if designList.count() > 0:
                for design in designList:
                    postOrUpdateAdData.delay('POST', design.id, userId)

    print('查询广告是否上传成功并上传未上传的广告的定时任务结束')


# 检查用户Token是否过期定时任务开始
@task
def checkUserToken():
    print('检查用户Token是否过期定时任务开始')
    userList = UserProfile.objects.all()
    for user in userList:
        if user.is_superuser != 1:
            userId = user.id
            n = HttpUtils.getHttp(Constants.GOALS_URL, userId)
            print(n.status_code)
            if n.status_code == 401:
                TokenUtils.getAPIToken(user.exo_name, user.exo_password)

    print('检查用户Token是否过期定时任务结束')


# 更新广告活动的投放率
@task
def updateSitesDataRate(userId):
    print('更新广告活动的投放率定时任务开始')
    ad_list = DesignAdList.objects.filter(adUser_id=userId)
    for ad in ad_list:
        postOrUpdateAdData('PUT', ad.id, userId)

    print('更新广告活动的投放率定时任务结束')



@task
def postOrUpdateSites(type, adId, sites, userId):
    print('上传或更新广告站点异步任务开始。。。。。')
    tarSitesList = []
    bloSitesList = []
    time.sleep(5)
    if not sites is None:
        for site in sites.split('\r\n'):
            if site.find('-') == 0:
                bloSitesList.append(site.replace('-', ''))
            else:
                tarSitesList.append(site)

    # 上传广告材料
    if type.find('POST') >= 0:
        # 上传站点
        print(json.dumps(bloSitesList))
        print(DesignAdList.objects.filter(id=adId)[0].campaign_id)
        postTarSites = HttpUtils.postSitesHttp(Constants.CAMPAIGNS_SITES_URL.format(adId, 'targeted'),
                                               json.dumps(tarSitesList), userId
                                               )
        postBloSites = HttpUtils.postSitesHttp(Constants.CAMPAIGNS_SITES_URL.format(adId, 'blocked'),
                                               json.dumps(bloSitesList), userId
                                               )

        print(str(postTarSites.status_code) + "  " + str(postBloSites.status_code))
        if postTarSites.status_code == 200 or postBloSites.status_code == 200:
            print('上传站点成功')
        print('上传站点定位：投放：{0}  屏蔽： {1}'.format(postTarSites.text, postBloSites.text))

    # 更新广告材料
    if type.find('PUT') >= 0:
        # 更新站点
        print(json.dumps(bloSitesList))
        putTarSites = HttpUtils.putSitesHttp(Constants.CAMPAIGNS_SITES_PUT_URL.format(adId, 'targeted'),
                                             json.dumps(tarSitesList), userId
                                             )
        putBloSites = HttpUtils.putSitesHttp(Constants.CAMPAIGNS_SITES_PUT_URL.format(adId, 'blocked'),
                                             json.dumps(bloSitesList), userId
                                             )
        print(str(putTarSites.status_code) + "  " + str(putBloSites.status_code))
        if putTarSites.status_code == 200 or putBloSites.status_code == 200:
            print('更新站点成功')
        print('更新站点定位：投放：{0}  屏蔽： {1}'.format(putTarSites.text, putBloSites.text))
    print('上传或更新广告站点异步任务结束。。。。。')


# 上传数据异步任务
@task
def postOrUpdateAdData(type, adId, userId,
                      # adName, adStyle, categoriesList,
                      # geographicLocationList, languagesList, adBrowsersList, operatingSystemList,
                      # mobileCarriersList, adDevicesList, priceModel,
                      # price, userMaxDailyBudget, isMaxDailyBudget,
                      # alltimeList,
                      # keywords, sites,
                      # impressionsEnabled, impressions,
                      # minutes,
                      # adAllLanguages, adAllBrowsers,
                      # adAllOperatingSystem, adAllMobileCarriers,
                      # adAllDevices,
                      # status
                       ):
    global adPostOrUpdate
    global keywordsList
    global budget_list
    global maxDailyBudget
    time.sleep(5)
    user = (UserProfile.objects.filter(id=userId))[0].username
    print('上传或更新用户{0}数据异步任务开始。。。。。'.format(user))

    ad = DesignAdList.objects.filter(id=adId)
    today = datetime.datetime.today()

    #上传广告
    tarSitesList = []
    bloSitesList = []
    cateList = []
    geoLocList = []
    langList = []
    browsersList = []
    operatingSysList = []
    moboileCarriersList = []
    devicesList = []
    monList = []
    tueList = []
    wedList = []
    thurList = []
    friList = []
    satList = []
    sunList = []
    alltimeList = []
    alltime = [
        0, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16,
        17, 18, 19, 20, 21,
        22, 23
    ]
    print(ad[0].categoriesList.count())
    if ad[0].categoriesList.count() > 0:
        for categories in ad[0].categoriesList.all():
            # print(categories.id)
            if categories.id == 1:
                continue
            if categories.id == 2:
                continue
            cateList.append(categories.id)

    if ad[0].geographicLocationList.count() > 0:
        for geographicLocation in ad[0].geographicLocationList.all():
            # print(geographicLocation.iso3)
            geoLocList.append(geographicLocation.iso3)

    if ad[0].languagesList.count() > 0:
        for languages in ad[0].languagesList.all():
            # print(languages.iso2)
            langList.append(languages.id)

    if ad[0].browsersList.count() > 0:
        for browser in ad[0].browsersList.all():
            browsersList.append(browser.id)

    if ad[0].operatingSystemList.count() > 0:
        for operatingSys in ad[0].operatingSystemList.all():
            operatingSysList.append(operatingSys.id)

    if ad[0].mobileCarriersList.count() > 0:
        for mobCarrier in ad[0].mobileCarriersList.all():
            moboileCarriersList.append(mobCarrier.id)

    if ad[0].devicesList.count() > 0:
        for device in ad[0].devicesList.all():
            devicesList.append(device.id)

    if ad[0].adAllTime:
        for perDate in range(1, 8):
            timeJson = {
                "day": perDate,
                "hours": alltime
            }
            alltimeList.append(timeJson)
    else:
        for mon in ad[0].mondayList.all():
            # print(mon.monTime.split(':')[0].strip())

            if mon.monTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 1,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                monList.append(mon.monTime.split(':')[0].strip())
        if len(monList) > 0:
            timeJson = {
                "day": 1,
                "hours": monList
            }
            alltimeList.append(timeJson)
        for tue in ad[0].tuesdayList.all():
            # print(tue.tueTime.split(':')[0].strip())
            if tue.tueTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 2,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                tueList.append(tue.tueTime.split(':')[0].strip())
        if len(tueList) > 0:
            timeJson = {
                "day": 2,
                "hours": tueList
            }
            alltimeList.append(timeJson)
        for wed in ad[0].wednesdayList.all():
            # print(wed.wedTime.split(':')[0].strip())

            if wed.wedTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 3,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                wedList.append(wed.wedTime.split(':')[0].strip())
        if len(wedList) > 0:
            timeJson = {
                "day": 3,
                "hours": wedList
            }
            alltimeList.append(timeJson)
        for thur in ad[0].thursdayList.all():
            # print(thur.thurTime.split(':')[0].strip())

            if thur.thurTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 4,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                thurList.append(thur.thurTime.split(':')[0].strip())
        if len(thurList) > 0:
            timeJson = {
                "day": 4,
                "hours": thurList
            }
            alltimeList.append(timeJson)
        for fri in ad[0].fridayList.all():
            # print(fri.friTime.split(':')[0].strip())

            if fri.friTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 5,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                friList.append(fri.friTime.split(':')[0].strip())
        if len(friList) > 0:
            timeJson = {
                "day": 5,
                "hours": friList
            }
            alltimeList.append(timeJson)
        for sat in ad[0].saturdayList.all():
            # print(sat.satTime.split(':')[0].strip())

            if sat.satTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 6,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                satList.append(sat.satTime.split(':')[0].strip())
        if len(satList) > 0:
            timeJson = {
                "day": 6,
                "hours": satList
            }
            alltimeList.append(timeJson)
        for sun in ad[0].sundayList.all():
            # print(sun.sunTime.split(':')[0].strip())

            if sun.sunTime.find('0:00 - 0:00') >= 0:
                timeJson = {
                    "day": 7,
                    "hours": alltime
                }
                alltimeList.append(timeJson)
                break
            else:
                sunList.append(sun.sunTime.split(':')[0].strip())
        if len(sunList) > 0:
            timeJson = {
                "day": 7,
                "hours": sunList
            }
            alltimeList.append(timeJson)

    if not ad[0].keywords is None:
        keywordsList = ad[0].keywords.split('\r\n')
    else:
        keywordsList = []

    if not ad[0].sites is None:
        for site in ad[0].sites.split('\r\n'):
            if site.find('-') == 0:
                bloSitesList.append(site.replace('-', ''))
            else:
                tarSitesList.append(site)

    if ad[0].isMaxDailyBudget:

        temp_budget = (float(ConversionUtils.meToExo(userId, float(ad[0].maxDailyBudget), today)))
        for temp in budget_list:
            if temp_budget > temp:
                maxDailyBudget = temp * 100
    else:
        maxDailyBudget = -1

    # 新建广告
    if type.find('POST') >= 0:
        print(type)

        adPostOrUpdate = HttpUtils.postHttp(Constants.CAMPAIGNS_URL,
                                            getAdJson(type, ad[0].adName, ad[0].adStyle, cateList,
                                                      geoLocList, langList, browsersList, operatingSysList,
                                                      moboileCarriersList, devicesList, int(ad[0].priceModel),
                                                      round(float(ConversionUtils.meToExo(userId, float(ad[0].price), today)) * 100, 2),
                                                      maxDailyBudget, alltimeList, keywordsList,
                                                      ad[0].impressionsEnabled, ad[0].impressions,
                                                      ad[0].minutes,
                                                      ad[0].adAllLanguages, ad[0].adAllBrowsers,
                                                      ad[0].adAllOperatingSystem, ad[0].adAllMobileCarriers,
                                                      ad[0].adAllDevices
                                                      ), False, userId)
    # 更新广告
    if type.find('PUT') >= 0:
        print(type)
        adPostOrUpdate = HttpUtils.putHttp(Constants.CAMPAIGNS_PUT_URL.format(ad[0].campaign_id),
                                            getAdJson(type, ad[0].adName, ad[0].adStyle, cateList,
                                                      geoLocList, langList, browsersList, operatingSysList,
                                                      moboileCarriersList, devicesList, int(ad[0].priceModel),
                                                      round(float(ConversionUtils.meToExo(userId, float(ad[0].price), today)) * 100, 2),
                                                      maxDailyBudget, alltimeList, keywordsList,
                                                      ad[0].impressionsEnabled, ad[0].impressions,
                                                      ad[0].minutes,
                                                      ad[0].adAllLanguages, ad[0].adAllBrowsers,
                                                      ad[0].adAllOperatingSystem, ad[0].adAllMobileCarriers,
                                                      ad[0].adAllDevices
                                                      ), userId)
    print(adPostOrUpdate)

    if not adPostOrUpdate is None:
        if adPostOrUpdate.status_code == 400:
            print(adPostOrUpdate.text)
            if adPostOrUpdate.text.find('Campaign pricing minimum') >= 0:
                ad.update(status=4)
            elif adPostOrUpdate.text.find('Campaign pricing for CPC cannot exceed') >= 0:
                ad.update(status=5)

            return 1


        if adPostOrUpdate.status_code == 200:
            print(adPostOrUpdate.text)
            adVarList = []
            if adPostOrUpdate.text.find('Campaign successfully updated') < 0:
                camp_id = adPostOrUpdate.text.split(':')[1].split('}')[0]
            else:
                camp_id = ad[0].campaign_id
            # print(camp_id)
            # 4是出价过低，5是CPC出价过高
            if ad[0].status == 4 and type.find('POST') >= 0:
                ad.update(campaign_id=camp_id, status=3)
            elif ad[0].status == 4 and type.find('PUT') >= 0:
                ad.update(status=3)
            elif ad[0].status != 4 and ad[0].status != 5 and type.find('POST') >= 0:
                ad.update(campaign_id=camp_id)
            elif ad[0].status == 5 and type.find('POST') >= 0:
                ad.update(campaign_id=camp_id, status=3)
            elif ad[0].status == 5 and type.find('PUT') >= 0:
                ad.update(status=3)

            # 更新浏览器、操作系统、移动运营商、设备等是否选所有
            if type.find('PUT') >= 0:
                if ad[0].adAllLanguages:
                    lan = HttpUtils.deleteHttp(Constants.LANGUAGES_DELETE_URL.format(camp_id), userId)
                    print('广告的语言选择所有操作：{0}：{1}'.format(lan.status_code, lan.text))
                if ad[0].adAllBrowsers:
                    bro = HttpUtils.deleteHttp(Constants.BROWSERS_DELETE_URL.format(camp_id), userId)
                    print('广告的浏览器选择所有操作：{0}：{1}'.format(bro.status_code, bro.text))
                if ad[0].adAllOperatingSystem:
                    oper = HttpUtils.deleteHttp(Constants.OPERATINGS_SYSTEM_DELETE_URL.format(camp_id), userId)
                    print('广告的操作系统选择所有操作：{0}：{1}'.format(oper.status_code, oper.text))
                if ad[0].adAllMobileCarriers:
                    carrier = HttpUtils.deleteHttp(Constants.CARRIERS_DELETE_URL.format(camp_id), userId)
                    print('广告的移动运营商选择所有操作：{0}：{1}'.format(carrier.status_code, carrier.text))
                if ad[0].adAllDevices:
                    dev = HttpUtils.deleteHttp(Constants.DEVICES_DELETE_URL.format(camp_id), userId)
                    print('广告的设备选择所有操作：{0}：{1}'.format(dev.status_code, dev.text))

            # urlCount = AdUrl.objects.filter(adCampaigns_id=designad.id).count()
            # 上传广告材料
            if type.find('POST') >= 0:
                # 需判断状态，待优化
                for adCreative in AdCreative.objects.filter(adCampaigns_id=adId):
                    # print(adCreative.id)
                    fileName = UserAdFileLibrary.objects.filter(file_id=adCreative.id_library_file)[0].file_name
                    # print('fimeName:::'+fileName)
                    # 判断是否已经上传过
                    if AdVariation.objects.filter(adCampaigns_id=adId,
                                                  id_library_file=adCreative.id_library_file,
                                                  url=AdUrl.objects.filter(adCampaigns_id=adId)[0].url
                                                  ).count() == 0:
                        adVar = HttpUtils.postVariationHttp(Constants.CAMPAIGNS_VARIATION_URL.format(camp_id),
                                                            getVariation(adCreative.id_library_file, fileName,
                                                                         fileName, AdUrl.objects.filter(
                                                                    adCampaigns_id=adId)[0].url
                                                                         ), userId
                                                            )
                        # print(adVar)
                        adVarList.append(adVar.text.split(':')[1].split('}')[0])

                        AdVariation.objects.update_or_create(varId=adVar.text.split(':')[1].split('}')[0],
                                                             id_library_file=adCreative.id_library_file,
                                                             adCampaigns_id=adId,
                                                             name=fileName,
                                                             description=fileName,
                                                             url=AdUrl.objects.filter(adCampaigns_id=adId)[0].url,
                                                             user_id=userId,
                                                             vari_url=UserAdFileLibrary.objects.filter(file_id=adCreative.id_library_file)[0].adMaterial
                                                             )
                        AdCreative.objects.filter(id_library_file=adCreative.id_library_file, adCampaigns_id=adId).update(
                            varId=adVar.text.split(':')[1].split('}')[0]
                        )
                        print('上传多个url匹配一个创意的广告材料：{0}'.format(adVar.text.split(':')[1].split('}')[0]))
                for adUrl in AdUrl.objects.filter(adCampaigns_id=adId):
                    # print(adUrl.id)
                    fileName = UserAdFileLibrary.objects.filter(file_id=AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file)[0].file_name
                    # print('fimeName:::' + fileName)
                    # 判断是否已经上传过
                    if AdVariation.objects.filter(adCampaigns_id=adId,
                                                  id_library_file=AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file,
                                                  url=adUrl.url
                                                  ).count() == 0:
                        adVar = HttpUtils.postVariationHttp(Constants.CAMPAIGNS_VARIATION_URL.format(camp_id),
                                                            getVariation(AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file, fileName,
                                                                         fileName, adUrl.url), userId)
                        # print(adVar)
                        adVarList.append(adVar.text.split(':')[1].split('}')[0])

                        file_id = AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file
                        AdVariation.objects.update_or_create(
                            id_library_file=file_id,
                            adCampaigns_id=adId,
                            varId=adVar.text.split(':')[1].split('}')[0],
                            name=fileName,
                            description=fileName,
                            url=adUrl.url,
                            user_id=userId,
                            vari_url=UserAdFileLibrary.objects.filter(file_id=file_id)[0].adMaterial
                            )
                        AdUrl.objects.filter(url=adUrl.url, adCampaigns_id=adId).update(varId=adVar.text.split(':')[1].split('}')[0])
                        print('上传多个创意匹配一个url的广告材料：{0}'.format(adVar.text.split(':')[1].split('}')[0]))

                # 上传站点
                print(json.dumps(bloSitesList))
                postTarSites = HttpUtils.postSitesHttp(Constants.CAMPAIGNS_SITES_URL.format(camp_id, 'targeted'),
                                               json.dumps(tarSitesList), userId
                                               )
                postBloSites = HttpUtils.postSitesHttp(Constants.CAMPAIGNS_SITES_URL.format(camp_id, 'blocked'),
                                               json.dumps(bloSitesList), userId
                                               )
                print(str(postTarSites.status_code) + "  " + str(postBloSites.status_code))
                print('上传站点定位：投放：{0}  屏蔽： {1}'.format(postTarSites.text, postBloSites.text))

            # 更新广告材料
            if type.find('PUT') >= 0:

                # 需判断状态，待优化
                for adCreative in AdCreative.objects.filter(adCampaigns_id=adId):
                    # print(adCreative.id)
                    fileName = UserAdFileLibrary.objects.filter(file_id=adCreative.id_library_file)[0].file_name
                    # print('fimeName:::' + fileName)
                    # 判断是否已经上传过
                    if AdVariation.objects.filter(adCampaigns_id=adId,
                                                  id_library_file=adCreative.id_library_file,
                                                  url=AdUrl.objects.filter(adCampaigns_id=adId)[0].url
                                                  ).count() == 0:

                        adVar = HttpUtils.putVariationHttp(Constants.CAMPAIGNS_VARIATION_URL.format(camp_id, adCreative.varId),
                                                            getVariation(adCreative.id_library_file, fileName,
                                                                         fileName, AdUrl.objects.filter(
                                                                    adCampaigns_id=adId)[0].url), userId)
                        print(adVar)
                        adVarList.append(adVar.text.split(':')[1].split('}')[0])

                        AdVariation.objects.update_or_create(varId=adVar.text.split(':')[1].split('}')[0],
                                                             id_library_file=adCreative.id_library_file,
                                                             adCampaigns_id=adId,
                                                             name=fileName,
                                                             description=fileName,
                                                             url=AdUrl.objects.filter(adCampaigns_id=adId)[0].url,
                                                             user_id=userId,
                                                             vari_url=UserAdFileLibrary.objects.filter(
                                                                 file_id=adCreative.id_library_file)[0].adMaterial
                                                             )
                        print('更新多个url匹配一个创意的广告材料：{0}'.format(adVar.text.split(':')[1].split('}')[0]))
                for adUrl in AdUrl.objects.filter(adCampaigns_id=adId):
                    print(adUrl.id)
                    fileName = UserAdFileLibrary.objects.filter(
                        file_id=AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file)[
                        0].file_name
                    print('fimeName:::' + fileName)
                    if AdVariation.objects.filter(adCampaigns_id=adId,
                                                  id_library_file=AdCreative.objects.filter(adCampaigns_id=adId)[
                                                      0].id_library_file,
                                                  url=adUrl.url
                                                  ).count() == 0:

                        adVar = HttpUtils.putVariationHttp(Constants.CAMPAIGNS_VARIATION_URL.format(camp_id, adUrl.varId),
                                                            getVariation(
                                                                AdCreative.objects.filter(adCampaigns_id=adId)[
                                                                    0].id_library_file, fileName,
                                                                fileName, adUrl.url), userId)
                        print(adVar)
                        adVarList.append(adVar.text.split(':')[1].split('}')[0])

                        file_id = AdCreative.objects.filter(adCampaigns_id=adId)[0].id_library_file
                        AdVariation.objects.update_or_create(
                            id_library_file=file_id,
                            adCampaigns_id=adId,
                            varId=adVar.text.split(':')[1].split('}')[0],
                            name=fileName,
                            description=fileName,
                            url=adUrl.url,
                            user_id=userId,
                            vari_url=UserAdFileLibrary.objects.filter(file_id=file_id)[0].adMaterial
                        )
                        print('更新多个创意匹配一个url的广告材料：{0}'.format(adVar.text.split(':')[1].split('}')[0]))

                # 更新站点
                print(json.dumps(bloSitesList))
                putTarSites = HttpUtils.putSitesHttp(Constants.CAMPAIGNS_SITES_PUT_URL.format(camp_id, 'targeted'),
                                                json.dumps(tarSitesList), userId
                                                )
                putBloSites = HttpUtils.putSitesHttp(Constants.CAMPAIGNS_SITES_PUT_URL.format(camp_id, 'blocked'),
                                                json.dumps(bloSitesList), userId
                                                )
                print(str(putTarSites.status_code) + "  " + str(putBloSites.status_code))
                print('更新站点定位：投放：{0}  屏蔽： {1}'.format(putTarSites.text, putBloSites.text))

            print(datetime.datetime.today())
            # 保存或更新新的字段
            ad.update(isPost=1)

        elif adPostOrUpdate.status_code == 500:
            print(adPostOrUpdate.text)
    print(datetime.datetime.today())
    print('上传或更新用户{0}数据异步任务结束。。。。。'.format(user))
    return 1
    pass


# 生成上传数据的json格式
def getAdJson(type, adName, adStyle, cateList, geoLocList, langList,
              browsersList,operatingSysList, moboileCarriersList,
              devicesList, priceModel, price, maxDailyBudget, alltimeList,
              keywordsList, impressionsEnabled, impressions, minutes,
              adAllLanguages, adAllBrowsers, adAllOperatingSystem, adAllMobileCarriers, adAllDevices):
    adJson = {}
    # adTye = AdvertiserAdType.objects.filter(name=adStyle)[0]
    # 上传广告材料
    if type.find('POST') >= 0:
        adJson = JsonUtils.getPostJson(adName, adStyle, cateList, geoLocList, langList,
              browsersList, operatingSysList, moboileCarriersList,
              devicesList, priceModel, price, maxDailyBudget, alltimeList,
              keywordsList, impressionsEnabled, impressions, minutes,
              adAllLanguages, adAllBrowsers, adAllOperatingSystem, adAllMobileCarriers, adAllDevices)

    # 更新广告材料
    if type.find('PUT') >= 0:
        adJson = JsonUtils.getPutJson(adName, adStyle, cateList, geoLocList, langList,
                                       browsersList, operatingSysList, moboileCarriersList,
                                       devicesList, priceModel, price, maxDailyBudget, alltimeList,
                                       keywordsList, impressionsEnabled, impressions, minutes,
                                       adAllLanguages, adAllBrowsers, adAllOperatingSystem, adAllMobileCarriers,
                                       adAllDevices)

    print(json.dumps(adJson, ensure_ascii=False))
    return adJson


# 生成上传广告材料的json格式
def getVariation(fileId, adName, keywords, adSite):
    # varJson = {
    #     'name': adName,
    #     'description': keywords,
    #     'url': adSite,
    #     'id_library_file': fileId
    # }
    # 此格式是postman生成，待优化
    varJson = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
              "name=\"name\"\r\n\r\n"+adName+"\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
              "name=\"description\"\r\n\r\n"+keywords+"\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
              "name=\"id_library_file\"\r\n\r\n"+str(fileId)+"\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
              "name=\"url\"\r\n\r\n"+str(adSite)+"\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    print(varJson)
    return varJson
    pass




