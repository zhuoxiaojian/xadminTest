import json

from designad.models import AdvertiserAdType


def getPostJson(adName, adStyle, cateList, geoLocList, langList,
              browsersList,operatingSysList, moboileCarriersList,
              devicesList, priceModel, price, maxDailyBudget, alltimeList,
              keywordsList, impressionsEnabled, impressions, minutes,
              adAllLanguages, adAllBrowsers, adAllOperatingSystem, adAllMobileCarriers, adAllDevices):
    adJson = {}
    # 获取广告类型
    adTye = AdvertiserAdType.objects.filter(name=adStyle)[0]
    if adAllLanguages and not adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and not adAllLanguages and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and not adAllLanguages and not adAllBrowsers and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllMobileCarriers and not adAllLanguages and not adAllBrowsers and not adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllBrowsers and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and not adAllBrowsers and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllMobileCarriers and not adAllOperatingSystem and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllLanguages and adAllDevices and not adAllOperatingSystem and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllOperatingSystem and not adAllLanguages and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllMobileCarriers and not adAllLanguages and not adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllMobileCarriers and not adAllLanguages and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllDevices and not adAllLanguages and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllMobileCarriers and adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllDevices and not adAllOperatingSystem and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and not adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and adAllMobileCarriers and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and adAllDevices and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem and not adAllLanguages:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllOperatingSystem and adAllDevices and not adAllLanguages and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllDevices and adAllOperatingSystem and adAllMobileCarriers and not adAllLanguages and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllLanguages and adAllOperatingSystem and adAllMobileCarriers and adAllDevices and not adAllBrowsers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and adAllDevices and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllLanguages:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and adAllMobileCarriers and adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif not adAllLanguages and not adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "campaign_type": {
                "type": 0,
                "value": 0
            },
            "advertiser_ad_type": adTye.id,
            "media_storage_template": json.loads(adTye.media_storage_templates)[0],
            "size": (adStyle.split('-')[1]).strip(),
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "retargeting": {
                "enabled": False,
                "goals": [{
                    "id": "",
                    "type": 0
                }]
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    return adJson


def getPutJson(adName, adStyle, cateList, geoLocList, langList,
              browsersList,operatingSysList, moboileCarriersList,
              devicesList, priceModel, price, maxDailyBudget, alltimeList,
              keywordsList, impressionsEnabled, impressions, minutes,
              adAllLanguages, adAllBrowsers, adAllOperatingSystem, adAllMobileCarriers, adAllDevices):
    adJson = {}
    # 获取广告类型
    adTye = AdvertiserAdType.objects.filter(name=adStyle)[0]
    if adAllLanguages and not adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and not adAllLanguages and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and not adAllLanguages and not adAllBrowsers and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllMobileCarriers and not adAllLanguages and not adAllOperatingSystem and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and not adAllBrowsers and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllMobileCarriers and not adAllOperatingSystem and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllLanguages and adAllDevices and not adAllOperatingSystem and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllOperatingSystem and not adAllLanguages and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllMobileCarriers and not adAllLanguages and not adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllMobileCarriers and not adAllLanguages and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllDevices and not adAllLanguages and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllMobileCarriers and adAllDevices and not adAllLanguages and not adAllOperatingSystem and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllDevices and not adAllOperatingSystem and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and not adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and adAllMobileCarriers and not adAllBrowsers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllOperatingSystem and adAllDevices and not adAllMobileCarriers and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem and not adAllLanguages:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllBrowsers and adAllOperatingSystem and adAllDevices and not adAllLanguages and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllDevices and adAllOperatingSystem and adAllMobileCarriers and not adAllLanguages and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    elif adAllLanguages and adAllOperatingSystem and adAllMobileCarriers and adAllDevices and not adAllBrowsers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and adAllDevices and not adAllMobileCarriers:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllOperatingSystem:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllMobileCarriers and adAllOperatingSystem and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllOperatingSystem and adAllBrowsers and adAllMobileCarriers and adAllDevices and not adAllLanguages:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif adAllLanguages and adAllBrowsers and adAllOperatingSystem and adAllMobileCarriers and adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },

            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }
    elif not adAllLanguages and not adAllBrowsers and not adAllOperatingSystem and not adAllMobileCarriers and not adAllDevices:
        adJson = {
            "name": adName,
            "media_type": {
                "type": 0,
                "format": json.loads(adTye.media_storage_templates)[0]
            },
            "categories": {
                "type": "targeted",
                "elements": cateList
            },
            "countries": {
                "type": "targeted",
                "elements": geoLocList
            },
            "languages": {
                "type": "targeted",
                "elements": langList
            },
            "browsers": {
                "type": "targeted",
                "elements": browsersList
            },
            "operating_systems": {
                "type": "targeted",
                "elements": operatingSysList
            },
            "carriers": {
                "type": "targeted",
                "elements": moboileCarriersList
            },
            "devices": {
                "type": "targeted",
                "elements": devicesList
            },
            "pricing": {
                "model": priceModel,
                "price": price
            },
            "frequency_capping": {
                "enabled": impressionsEnabled,
                "impressions": impressions,
                "minutes": minutes
            },
            "max_daily_budget": maxDailyBudget,
            "idgroup": 0,
            "day_parting": {
                "timezone": "Asia/Shanghai",
                "parting": alltimeList
            },
            "sites": {
                "type": "targeted",
                "elements": [
                    ""
                ]
            },
            "keywords": {
                "type": "targeted",
                "elements": keywordsList
            },
            "optimization_rule": 0
        }

    return adJson