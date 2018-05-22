import time
from time import mktime

import datetime

from costreport.models import CostDailyReport, CostHourReport
from users.models import UserProfile, AdPriceRate
from utils import ConversionUtils
from utils.CacheUtils import write_adrecode_to_cache

__author__ = 'cwd'
__date__ = '2018/3/7 15:48'

import json

from utils.Constants import Constants

from designad.models import Categories, GeographicLocation, Languages, Browsers, MobileCarriers, OperatingSystems, \
    Devices, AdvertiserAdType, DesignAdList, AdVariation, AdGoals, SitesData, UserAdFileLibrary
from collectiondata.models import MinimumPrices
from costtrendreport.models import CostDailyTrendReport,CostHourTrendReport
from utils.HttpUtils import HttpUtils


class InitData(object):

    # 获取所有的广告信息
    def getAllCamp(none):
        try:
            url = Constants.CAMPAIGNS_URL
            userList = UserProfile.objects.all()
            for user in userList:
                print(user.id)
                print(user.username)
                userId = user.id
                n = HttpUtils.getHttp(url, userId)
                if not n is None:
                    if n.status_code == 200:
                        body = json.loads(n.text)
                        result = body['result']
                        for designAd in result:

                            # if not DesignAdList.objects.filter(campaign_id=result[designAd]['id']).exists():
                            #     # campaign = DesignAdList.objects.get(campaign_id=result[designad]['id'])
                            #     designAdList = DesignAdList()
                            #     designAdList.campaign_id = result[designAd]['id']
                            #     designAdList.adUser_id = userId
                            #     designAdList.adName = result[designAd]['name']
                            #     designAdList.maxDailyBudget = result[designAd]['max_daily_budget_reset']
                            #     designAdList.adStyle = AdvertiserAdType.objects.filter(id=result[designAd]['advertiser_ad_type'])[0].name
                            #     designAdList.priceModel = result[designAd]['pricing_model']
                            #     designAdList.status = result[designAd]['status']
                            #     designAdList.checked = result[designAd]['checked']
                            #     # designAdList.price = ConversionUtils.exoToMe(userId, result[designad]['price'], campaign.created_at)
                            #     DesignAdList.save(designAdList)
                            if DesignAdList.objects.filter(campaign_id=result[designAd]['id']).exists():
                                # campaign = DesignAdList.objects.get(campaign_id=result[designad]['id'])
                                DesignAdList.objects.filter(campaign_id=result[designAd]['id']).update(
                                                                                              priceModel=result[designAd]['pricing_model'],
                                                                                              adStyle=AdvertiserAdType.objects.filter(id=result[designAd]['advertiser_ad_type'])[0].name,
                                                                                              status=result[designAd]['status'],
                                                                                              checked=result[designAd]['checked'],
                                                                                              isPost=1,
                                                                                              # price=ConversionUtils.exoToMe(userId, result[designad]['price'], campaign.created_at)
                                                                                              )
                    # 每次循环结束睡眠10秒
                    print('睡眠10s')
                    time.sleep(10)
                    print('睡眠结束')
        except Exception as ex:
            print(ex)

    # 获取用户创意
    def getUserAdFile(none):
        url = Constants.USER_FILE_URL
        userList = UserProfile.objects.all()
        for user in userList:

            userId = user.id
            n = HttpUtils.getHttp(url, userId)
            if not n is None:
                if n.status_code == 200:
                    body = json.loads(n.text)
                    result = body['result']
                    for userAdFile in result:

                        # if UserAdFileLibrary.objects.filter(file_id=userAdFile.get('id')).count() < 0:
                            print(userAdFile)
                            userAdFileLibrary = UserAdFileLibrary()
                            userAdFileLibrary.user_id = userId
                            userAdFileLibrary.file_id = userAdFile.get('id')
                            userAdFileLibrary.file_name = userAdFile.get('file_name')
                            userAdFileLibrary.type = userAdFile.get('type')
                            userAdFileLibrary.width = userAdFile.get('width')
                            userAdFileLibrary.height = userAdFile.get('height')
                            userAdFileLibrary.file_extension = userAdFile.get('file_extension')
                            userAdFileLibrary.file_size = userAdFile.get('file_size_public')
                            userAdFileLibrary.url = userAdFile.get('url')
                            userAdFileLibrary.created_at = userAdFile.get('created_at')
                            userAdFileLibrary.updated_at = userAdFile.get('updated_at')
                            UserAdFileLibrary.save(userAdFileLibrary)


    # 获取分类
    def getCategories(none):
        url = Constants.CATEGORIES_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for category in result:
                    # print(category)
                    if category.get('parent') != 0:
                        categories = Categories()
                        categories.id = category.get('id')
                        categories.name = category.get('name')
                        categories.parent = category.get('parent')
                        Categories.save(categories)

    # 获取浏览器
    def getBrowsers(none):
        url = Constants.BROWSERS_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                print(result)
                for browser in result:
                    # print(browser)
                    browsers = Browsers()
                    browsers.id = browser.get('id')
                    browsers.name = browser.get('name')
                    Browsers.save(browsers)

    # 获取设备
    def getDevices(none):
        url = Constants.DEVICES_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for device in result:
                    # print(device)
                    devices = Devices()
                    devices.id = device.get('id')
                    devices.name = device.get('name')
                    Devices.save(devices)

    # 获取操作系统
    def getOperatingSystem(none):
        url = Constants.OPERATINGS_SYSTEM_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for operatingSystem in result:
                    # print(operatingSystem)
                    operatingSystems = OperatingSystems()
                    operatingSystems.id = operatingSystem.get('id')
                    operatingSystems.name = operatingSystem.get('name')
                    operatingSystems.type = operatingSystem.get('type')
                    OperatingSystems.save(operatingSystems)

    # 获取移动代理商
    def getMobileCarriers(none):
        url = Constants.CARRIERS_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for mobileCarrier in result:
                    # print(mobileCarrier)
                    mobileCarriers = MobileCarriers()
                    mobileCarriers.id = mobileCarrier.get('id')
                    mobileCarriers.name = mobileCarrier.get('name')
                    mobileCarriers.country_id = mobileCarrier.get('country_id')
                    mobileCarriers.enabled = mobileCarrier.get('enabled')
                    MobileCarriers.save(mobileCarriers)

    # 获取地理位置
    def getGeoLoc(none):
        url = Constants.COUNTRY_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for geographicLocationDate in result:
                    # print(geographicLocationDate)
                    if geographicLocationDate.get('id') != 0:
                        geographicLocation = GeographicLocation()
                        geographicLocation.id = geographicLocationDate.get('id')
                        geographicLocation.short_name = geographicLocationDate.get('short_name')
                        geographicLocation.long_name = geographicLocationDate.get('long_name')
                        geographicLocation.iso2 = geographicLocationDate.get('iso2')
                        geographicLocation.iso3 = geographicLocationDate.get('iso3')
                        GeographicLocation.save(geographicLocation)

    # 获取语言
    def getLanguages(none):
        url = Constants.LANGUAGES_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for lang in result:
                    # print(lang)
                    languages = Languages()
                    languages.id = lang.get('id')
                    languages.name = lang.get('name')
                    languages.iso2 = lang.get('iso2')
                    languages.iso2_two = lang.get('iso2_two')
                    languages.save(lang)

    # 获取最低价格
    def getMinimumPrices(none):
        url = Constants.MINIMUM_PRICES_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                # print(result)
                for miniPrices in result:

                    minimumPrices = MinimumPrices()
                    minimumPrices.format = miniPrices.get('format')
                    minimumPrices.geo = miniPrices.get('country')
                    minimumPrices.category = miniPrices.get('category')
                    minimumPrices.network_selection_type = miniPrices.get('network_selection_type')
                    minimumPrices.web_cpc = miniPrices.get('web_cpc')
                    minimumPrices.mobile_cpc = miniPrices.get('mobile_cpc')
                    minimumPrices.web_cpm = miniPrices.get('web_cpm')
                    minimumPrices.mobile_cpm = miniPrices.get('mobile_cpm')
                    MinimumPrices.save(minimumPrices)

    # 获取广告类型
    def getAdType(none):
        url = Constants.ADVERTISER_AD_TYPES_URL
        user = UserProfile.objects.all()[0]
        n = HttpUtils.getHttp(url, user.id)
        if not n is None:
            if n.status_code == 200:
                body = json.loads(n.text)
                result = body['result']
                for adType in result:
                    # print(adType)
                    advertiserAdType = AdvertiserAdType()
                    advertiserAdType.id = adType.get('id')
                    advertiserAdType.name = adType.get('name')
                    advertiserAdType.media_storage_templates = json.dumps(adType.get('media_storage_templates'))
                    AdvertiserAdType.save(advertiserAdType)

    # 获取材料状态
    def getVariStatus(campaignid, userId):
        try:
            url = Constants.CAMPAIGNS_VARIATION_URL.format(campaignid)

            n = HttpUtils.getHttp(url, userId)
            print(n)
            if not n is None:
                if n.status_code == 200:
                    body = json.loads(n.text)
                    result = body['variations']
                    for adVariStatus in result:
                        if AdVariation.objects.filter(varId=adVariStatus['idvariation']).exists():
                            AdVariation.objects.filter(varId=adVariStatus['idvariation']).update(status=adVariStatus['variation_status'])
                        else:
                            adVariation = AdVariation()
                            adVariation.name = adVariStatus['name']
                            adVariation.user_id = userId
                            adVariation.description = adVariStatus['description']
                            adVariation.url = adVariStatus['url']
                            adVariation.adCampaigns_id = DesignAdList.objects.get(campaign_id=campaignid).id
                            adVariation.id_library_file = adVariStatus['idvariations_file']
                            adVariation.status = adVariStatus['variation_status']
                            adVariation.varId = adVariStatus['idvariation']
                            AdVariation.save(adVariation)

                # 每次循环结束睡眠5秒
                time.sleep(5)
        except Exception as ex:
            print(ex)

    # 获取Goals
    def getGoals(none):
        try:
            url = Constants.GOALS_URL
            userList = UserProfile.objects.all()
            for user in userList:
                userId = user.id
                n = HttpUtils.getHttp(url, userId)
                if not n is None:
                    if n.status_code == 200:
                        if n.text.find('Goals could not be found') < 0:
                            body = json.loads(n.text)
                            result = body['result']
                            for goal in result:
                                if AdGoals.objects.filter(goalId=goal.get('id')).count() > 0:
                                    scp = '<!-- START MonAdvert  Goal Tag | '+goal.get('name')+' --><script type="text/javascript" src="http://service.monadvert.com/tag_gen.js" data-goal="' + goal.get('id') + '"></script><!-- END MonAdvert  Goal Tag | '+goal.get('name')+' -->'
                                    AdGoals.objects.filter(goalId=goal.get('id')).update(
                                        goalId=goal.get('id'),
                                        name=goal.get('name'),
                                        seq=goal.get('seq'),
                                        idUser=goal.get('iduser'),
                                        order=goal.get('order'),
                                        coa=goal.get('coa'),
                                        goalScript=scp
                                    )
                                else:
                                    adGoals = AdGoals()
                                    adGoals.goalId = goal.get('id')
                                    adGoals.name = goal.get('name')
                                    adGoals.seq = goal.get('seq')
                                    adGoals.idUser = goal.get('iduser')
                                    adGoals.user_id = userId
                                    adGoals.order = goal.get('order')
                                    adGoals.coa = goal.get('coa')
                                    scp = '<!-- START MonAdvert  Goal Tag | '+goal.get('name')+' --><script type="text/javascript" src="http://service.monadvert.com/tag_gen.js" data-goal="' + goal.get('id') + '"></script><!-- END MonAdvert  Goal Tag | '+goal.get('name')+' -->'
                                    adGoals.goalScript = scp
                                    AdGoals.save(adGoals)
                    # 每次循环结束睡眠5秒
                    time.sleep(5)
        except Exception as ex:
            print(ex)


    # 获取广告日消费数据
    def getAdStatistics(campaignid, userId):
        try:
            for i in range(0, 8):
                day = datetime.date.today()
                oneday = datetime.timedelta(days=i)
                today = day - oneday
                # today = datetime.date.today()

                dateurl = Constants.STATISTICS_ADVERTISER_DATE.format(campaignid, today, today)
                print(dateurl)
                n = HttpUtils.getHttp(dateurl, userId)
                if n.status_code == 200:
                    body = json.loads(n.text)
                    result = body['result']
                    if not result is []:
                        print(result)
                        for costDailyData in result:
                            if DesignAdList.objects.filter(campaign_id=int(campaignid)).count() > 0:
                                # 将其转换为时间数组
                                dailyTimeArray = datetime.datetime.strptime(costDailyData.get('ddate'), '%Y-%m-%d')
                                print(dailyTimeArray)
                                campaignId = DesignAdList.objects.filter(campaign_id=campaignid)[0].id
                                rate = ConversionUtils.getRate(userId, dailyTimeArray)
                                deliveryRate = rate.get('deliveryRate')
                                # 如果广告数据已经存在则更新数据
                                if CostDailyTrendReport.objects.filter(adCampaigns_id=campaignId,
                                                                       date=costDailyData.get('ddate')).count() > 0:

                                    CostDailyTrendReport.objects.filter(adCampaigns_id=campaignId,
                                                                        date=costDailyData.get('ddate')).update(cost=costDailyData.get('cost'),
                                                                                                                deliveryRate=deliveryRate,
                                                                                                                )
                                # 如果广告数据不存在则添加数据
                                else:
                                    if DesignAdList.objects.filter(campaign_id=campaignid).count() > 0:
                                        costDailyTrendReport = CostDailyTrendReport()
                                        costDailyTrendReport.adUser_id = DesignAdList.objects.filter(campaign_id=campaignid)[0].adUser_id
                                        costDailyTrendReport.adCampaigns_id = campaignId
                                        costDailyTrendReport.cost = costDailyData.get('cost')
                                        costDailyTrendReport.deliveryRate = deliveryRate
                                        costDailyTrendReport.date = costDailyData.get('ddate')

                                        CostDailyTrendReport.save(costDailyTrendReport)

                                if costDailyData.get('clicks') != 0:
                                    avgCpc = float(costDailyData.get('cost') / costDailyData.get('clicks'))
                                else:
                                    avgCpc = '0.00'

                                if costDailyData.get('ctr') != 0:
                                    dailyCtr = round(costDailyData.get('ctr'), 2)
                                    print('换算日CTR：：：：：'+str(dailyCtr)+'  原始日CTR::::'+ str(costDailyData.get('ctr')))
                                else:
                                    dailyCtr = 0.00

                                if CostDailyReport.objects.filter(adCampaigns_id=campaignId, date=costDailyData.get('ddate')).count() > 0:
                                    CostDailyReport.objects.filter(adCampaigns_id=campaignId,
                                                                   date=costDailyData.get('ddate')).update(
                                        cost=costDailyData.get('cost'),
                                        impressions=costDailyData.get('impressions'),
                                        clicks=costDailyData.get('clicks'),
                                        avgCpc=avgCpc,
                                        deliveryRate=deliveryRate,
                                        ctr=dailyCtr
                                        )
                                else:
                                    costDailyReport = CostDailyReport()
                                    costDailyReport.adUser_id = DesignAdList.objects.filter(campaign_id=campaignid)[0].adUser_id
                                    costDailyReport.adCampaigns_id = campaignId
                                    costDailyReport.cost = costDailyData.get('cost')
                                    costDailyReport.impressions = costDailyData.get('impressions')
                                    costDailyReport.clicks = costDailyData.get('clicks')
                                    costDailyReport.avgCpc = avgCpc
                                    costDailyReport.ctr = dailyCtr
                                    costDailyReport.deliveryRate = deliveryRate
                                    costDailyReport.date = costDailyData.get('ddate')
                                    CostDailyReport.save(costDailyReport)
        except Exception as ex:
            print(ex)

    # 获取分时数据
    def getHourData(campaignid, userId):
        try:
            for i in range(0, 8):
                day = datetime.date.today()
                oneday = datetime.timedelta(days=i)
                today = day - oneday #datetime.date.today()
                # yesterday = today - datetime.timedelta(days=1)
                hoururl = Constants.STATISTICS_ADVERTISER_HOUR.format(campaignid, today, today)
                print(hoururl)
                n = HttpUtils.getHttp(hoururl, userId)
                print(n)
                if n.status_code == 200:
                    body = json.loads(n.text)
                    result = body.get('result')
                    print('时间：：{0}'.format(result))
                    if not result is []:
                        for costHourData in result:
                            dateTime = datetime.datetime.strptime(str(today) + ' ' + str(costHourData.get('hour')),
                                                                  '%Y-%m-%d %H')
                            rate = ConversionUtils.getRate(userId, dateTime)
                            deliveryRate = rate.get('deliveryRate')
                            print(dateTime)
                            campaignId = DesignAdList.objects.filter(campaign_id=campaignid)[0].id
                            if CostHourTrendReport.objects.filter(
                                    adCampaigns_id=campaignId,
                                    date=dateTime).count() > 0:
                                CostHourTrendReport.objects.filter(adCampaigns_id=campaignId, date=dateTime).update(
                                    cost=costHourData.get('cost'),
                                    deliveryRate=deliveryRate
                                )
                            else:
                                # 存储已获取过的广告数据，获取时间的数据需要判断，每日的数据不用
                                # write_adrecode_to_cache(str(campaignid).join(str(timeStamp)), 1)
                                print(campaignid)
                                if DesignAdList.objects.filter(campaign_id=campaignid).count() > 0:
                                    costHourTrendReport = CostHourTrendReport()

                                    costHourTrendReport.adUser_id = DesignAdList.objects.filter(campaign_id=campaignid)[0].adUser_id
                                    costHourTrendReport.adCampaigns_id = campaignId
                                    costHourTrendReport.cost = costHourData.get('cost')
                                    costHourTrendReport.deliveryRate = deliveryRate
                                    costHourTrendReport.date = dateTime
                                    print(costHourTrendReport)
                                    CostHourTrendReport.save(costHourTrendReport)

                            if costHourData.get('clicks') != 0:
                                avgCpc = (costHourData.get('cost') / costHourData.get('clicks'))
                            else:
                                avgCpc = '0.00'

                            if costHourData.get('ctr') != 0:
                                hourCtr = round(costHourData.get('ctr'), 2)
                                print('换算分时CTR：：：：：' + str(hourCtr) + '  原始分时CTR::::' + str(costHourData.get('ctr')))
                            else:
                                hourCtr = 0.00
                            if CostHourReport.objects.filter(
                                    adCampaigns_id=DesignAdList.objects.filter(campaign_id=campaignid)[0].id,
                                    date=dateTime).count() > 0:
                                CostHourReport.objects.filter(
                                    adCampaigns_id=DesignAdList.objects.filter(campaign_id=campaignid)[0].id,
                                    date=dateTime).update(
                                    cost=costHourData.get('cost'),
                                    impressions=costHourData.get('impressions'),
                                    clicks=costHourData.get('clicks'),
                                    avgCpc=avgCpc,
                                    deliveryRate=deliveryRate,
                                    ctr=hourCtr
                                )
                            else:
                                print(campaignid)
                                if DesignAdList.objects.filter(campaign_id=campaignid).count() > 0:
                                    costHourReport = CostHourReport()
                                    costHourReport.adUser_id = DesignAdList.objects.filter(campaign_id=campaignid)[0].adUser_id
                                    costHourReport.adCampaigns_id = DesignAdList.objects.filter(campaign_id=campaignid)[0].id
                                    costHourReport.cost = costHourData.get('cost')
                                    costHourReport.date = dateTime
                                    costHourReport.impressions = costHourData.get('impressions')
                                    costHourReport.clicks = costHourData.get('clicks')
                                    costHourReport.avgCpc = avgCpc
                                    costHourReport.deliveryRate = deliveryRate
                                    costHourReport.ctr = hourCtr
                                    print(costHourReport)
                                    CostHourReport.save(costHourReport)
        except Exception as ex:
            print(ex)

    # 获取站点数据
    def getSitesData(userId):
        try:
            for i in range(0, 8):
                day = datetime.date.today()
                oneday = datetime.timedelta(days=i)
                today = day-oneday #datetime.date.today()
                countSites = HttpUtils.getHttp(Constants.STATISTICS_ADVERTISER_SITES_COUNT.format(today, today), userId)
                if countSites.status_code == 200 and not type(json.loads(countSites.text).get('request_metadata')) is list:
                    count = json.loads(countSites.text).get('request_metadata').get('count')
                    # print(count)
                    num = int(count/1000) + 1
                    print(num)
                    for j in range(0, num):
                        sitesUrl = Constants.STATISTICS_ADVERTISER_SITES_GOALS.format(today, today, (j * 1000))
                        print(sitesUrl)
                        n = HttpUtils.getHttp(sitesUrl, userId)
                        # print(n)
                        print(sitesUrl)
                        if not n is None:
                            print(n.status_code)
                            if n.status_code == 200:
                                # 转时间
                                dailyTimeArray = datetime.datetime.strptime(str(today),
                                                                            '%Y-%m-%d')
                                print(dailyTimeArray)
                                rate = ConversionUtils.getRate(userId, dailyTimeArray)
                                deliveryRate = rate.get('deliveryRate')

                                body = json.loads(n.text)
                                result = body.get('result')
                                # print(result)
                                if not result is []:
                                    adGoals_count = AdGoals.objects.filter(user_id=userId).count()
                                    # print(adGoals_count)
                                    for siteData in result:
                                        goalList = []
                                        ecpaList = []
                                        # print(siteData)

                                        if float(siteData.get('ctr')) != 0:
                                            siteCtr = round(float(siteData.get('ctr')), 2)
                                            # print('站点CTR：：：：：' + str(siteCtr) + '  站点CTR::::' + str(siteData.get('ctr')))
                                        else:
                                            siteCtr = 0.00

                                        if str(siteData.get('site_hostname')).find('exoclick') > 0:
                                            site_hostname = 'http://service.monadvert.com/'

                                        else:
                                            site_hostname = siteData.get('site_hostname')
                                        if DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign')).count() > 0:
                                            if SitesData.objects.filter(adCampaigns_id=DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign'))[0].id,
                                                                        site_hostname=site_hostname,
                                                                        date=today).count() > 0:

                                                if adGoals_count > 0:
                                                    goals = siteData.get('goals').get('data')

                                                    for goal in goals:
                                                        goalList.append(goals[goal]['volume'])
                                                        ecpaList.append(goals[goal]['ecpa'])
                                                    if len(goalList) == 0:
                                                        for i in range(0, 4):
                                                            goalList.append(0)
                                                            ecpaList.append(0)
                                                    elif len(goalList) == 1:
                                                        for i in range(0, 3):
                                                            goalList.append(0)
                                                            ecpaList.append(0)
                                                    elif len(goalList) == 2:
                                                        for i in range(0, 2):
                                                            goalList.append(0)
                                                            ecpaList.append(0)
                                                    elif len(goalList) == 3:
                                                        for i in range(0, 1):
                                                            goalList.append(0)
                                                            ecpaList.append(0)
                                                else:
                                                    for i in range(0, 4):
                                                        goalList.append(0)
                                                        ecpaList.append(0)
                                                if siteData.get('cpc') != 0:
                                                    avgCpc = (siteData.get('cost') / siteData.get('clicks'))

                                                else:
                                                    avgCpc = '0.00'

                                                if siteData.get('impressions') != 0:
                                                    avgCpm = siteData.get('cost') / (siteData.get('impressions')/1000)
                                                else:
                                                    avgCpm = '0.00'
                                                # print('更新：：：' + site_hostname)
                                                SitesData.objects.filter(adCampaigns_id=DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign'))[0].id,
                                                                                   site_hostname=site_hostname,
                                                                                   date=today).update(cost=siteData.get('cost'),
                                                                                                      clicks=siteData.get('clicks'),
                                                                                                      impressions=siteData.get('impressions'),
                                                                                                      adCampaigns_id=DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign'))[0].id,
                                                                                                      ctr=siteCtr,
                                                                                                      cpm=siteData.get('cpm'),
                                                                                                      cpv=siteData.get('cpv'),
                                                                                                      cpc=siteData.get('cpc'),
                                                                                                      avgCpc=avgCpc,
                                                                                                      avgCpm=avgCpm,
                                                                                                      deliveryRate=deliveryRate,
                                                                                                      G1=goalList[0],
                                                                                                      ecpa1=ecpaList[0],
                                                                                                      G2=goalList[1],
                                                                                                      ecpa2=ecpaList[1],
                                                                                                      G3=goalList[2],
                                                                                                      ecpa3=ecpaList[2],
                                                                                                      G4=goalList[3],
                                                                                                      ecpa4=ecpaList[3],
                                                                                                      date=str(today)
                                                                                                      )
                                            elif SitesData.objects.filter(adCampaigns_id=DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign'))[0].id,
                                                                        site_hostname=site_hostname,
                                                                        date=today).count() <= 0:
                                                # 存储已获取过的广告数据，获取时间的数据需要判断，每日的数据不用
                                                # write_adrecode_to_cache(str(campaignid).join(str(timeStamp)), 1)
                                                # print('插入：：：' + site_hostname)

                                                sitesData = SitesData()
                                                if adGoals_count > 0:
                                                    goals = siteData.get('goals').get('data')
                                                    for goal in goals:
                                                        if AdGoals.objects.filter(user_id=userId).count() > 0:

                                                            for i in range(0, AdGoals.objects.filter(user_id=userId).count()):
                                                                if i == 0:
                                                                    sitesData.G1 = goals[goal]['volume']
                                                                    sitesData.ecpa1 = goals[goal]['ecpa']
                                                                    # print(goal)
                                                                    # print(G1)
                                                                    # print(ecpa1)
                                                                elif i == 1:
                                                                    sitesData.G2 = goals[goal]['volume']
                                                                    sitesData.ecpa2 = goals[goal]['ecpa']
                                                                    # print('g2::' + str(G2))
                                                                    # print(ecpa2)
                                                                elif i == 2:
                                                                    sitesData.G3 = goals[goal]['volume']
                                                                    sitesData.ecpa3 = goals[goal]['ecpa']

                                                                    # print('g3::' + str(G3))
                                                                    # print(ecpa3)
                                                                elif i == 3:
                                                                    sitesData.G4 = goals[goal]['volume']
                                                                    sitesData.ecpa4 = goals[goal]['ecpa']

                                                                    # print('g4::' + str(G4))
                                                                    # print(ecpa4)
                                                # print(siteData)

                                                sitesData.site_hostname = site_hostname
                                                sitesData.cost = siteData.get('cost')
                                                sitesData.deliveryRate = deliveryRate
                                                sitesData.clicks = siteData.get('clicks')
                                                sitesData.impressions = siteData.get('impressions')
                                                sitesData.adCampaigns_id = DesignAdList.objects.filter(campaign_id=siteData.get('idcampaign'))[0].id

                                                sitesData.ctr = siteCtr
                                                sitesData.cpm = siteData.get('cpm')
                                                sitesData.cpv = siteData.get('cpv')
                                                sitesData.cpc = siteData .get('cpc')
                                                if siteData.get('cpc') != 0:
                                                    sitesData.avgCpc = (siteData.get('cost') / siteData.get('clicks'))
                                                else:
                                                    sitesData.avgCpc = '0.00'

                                                if siteData.get('impressions') != 0:
                                                    sitesData.avgCpm = siteData.get('cost') / (siteData.get('impressions') / 1000)

                                                else:
                                                    sitesData.avgCpm = '0.00'

                                                sitesData.impressions = siteData.get('impressions')
                                                sitesData.user_id = userId
                                                sitesData.date = str(today)
                                                SitesData.save(sitesData)
        except Exception as ex:
            print(ex)