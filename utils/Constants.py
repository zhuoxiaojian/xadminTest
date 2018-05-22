__author__ = 'cwd'
__date__ = '2018/3/7 11:22'


class Constants(object):
    LOGIN_URL = 'https://api.exoclick.com/v2/login'

    # 广告活动操作URL
    CAMPAIGNS_URL = 'https://api.exoclick.com/v2/campaigns'
    CAMPAIGNS_GROUPS_URL = 'https://api.exoclick.com/v2/campaigns/groups'
    CAMPAIGNS_COUNTRY_URL = 'https://api.exoclick.com/v2/campaigns/{0}/targeted/countries'
    CAMPAIGNS_VARIATION_URL = 'https://api.exoclick.com/v2/campaigns/{0}/variation'
    # https://api.exoclick.com/v2/campaigns/{campaignid}/{targeting_type}/keywords
    # targeting_type可为targeted(定向投放)、blocked（封锁投放）
    CAMPAIGNS_KEYWORDS_URL = 'https://api.exoclick.com/v2/campaigns/{0}/{1}/keywords'
    CAMPAIGNS_IP_RANGES_URL = 'https://api.exoclick.com/v2/campaigns/{0}/{1}/ip_ranges'
    # {1}可填targeted/blocked
    CAMPAIGNS_SITES_URL = 'https://api.exoclick.com/v2/campaigns/{0}/{1}/sites'
    ADVERTISER_AD_TYPES_URL = 'https://api.exoclick.com/v2/collections/advertiser-ad-types'


    # 获取平台接口数据URL
    CATEGORIES_URL = 'https://api.exoclick.com/v2/collections/categories'
    VARIATION_URL = 'https://api.exoclick.com/v2/campaigns/{0}/variation'
    COUNTRY_URL = 'https://api.exoclick.com/v2/collections/countries?limit=300&offset=0'
    AD_TYPE_URL = 'https://api.exoclick.com/v2/collections/advertiser-ad-types'
    MINIMUM_PRICES_URL = 'https://api.exoclick.com/v2/collections/minimum-prices'
    DAILY_BUDGET_URL = 'https://api.exoclick.com/v2/collections/daily-budget'
    LANGUAGES_URL = 'https://api.exoclick.com/v2/collections/languages?limit=200&offset=0'
    DEVICES_URL = 'https://api.exoclick.com/v2/collections/devices?limit=100&offset=0'
    OPERATINGS_SYSTEM_URL = 'https://api.exoclick.com/v2/collections/operating-systems'
    CARRIERS_URL = 'https://api.exoclick.com/v2/collections/carriers?limit=600&offset=0'
    BROWSERS_URL = 'https://api.exoclick.com/v2/collections/browsers?limit=100&offset=0'
    GOALS_URL = 'https://api.exoclick.com/v2/goals'
    GOALS_UPDATE_OR_DELETE_URL = 'https://api.exoclick.com/v2/goals/{0}'
    USER_FILE_URL = 'https://api.exoclick.com/v2/library/file'


    # 获取用户数据
    STATISTICS_ADVERTISER_DATE = 'https://api.exoclick.com/v2/statistics/advertiser/date?campaignid={0}&date-to={1}&date-from={2}&include=goals&limit=1000&offset=0'
    STATISTICS_ADVERTISER_HOUR = 'https://api.exoclick.com/v2/statistics/advertiser/hour?campaignid={0}&date-to={1}&date-from={2}&include=goals&limit=1000&offset=0'
    STATISTICS_ADVERTISER_SITES_GOALS = 'https://api.exoclick.com/v2/statistics/advertiser/site?date-to={0}&date-from={1}&include=goals&additional_group_by=campaignid&limit=1000&offset={2}'
    STATISTICS_ADVERTISER_SITES_COUNT = 'https://api.exoclick.com/v2/statistics/advertiser/site?date-to={0}&date-from={1}&additional_group_by=campaignid&include=count'
    STATISTICS_ADVERTISER_DATE_ACOUNT = 'https://api.exoclick.com/v2/statistics/advertiser/date?date-to={0}&date-from={1}&limit=1000&offset=0'

    USER_ACOUNT_URL = 'https://api.exoclick.com/v2/user'

    # 上传和获取文件url
    IMAGE_LIBRARY_URL = 'https://api.exoclick.com/v2/library/file'

    # PUT接口
    CAMPAIGNS_PUT_URL = 'https://api.exoclick.com/v2/campaigns/{0}'
    CAMPAIGNS_PALY_URL = 'https://api.exoclick.com/v2/campaigns/play'
    CAMPAIGNS_DELETE_URL = 'https://api.exoclick.com/v2/campaigns/delete'
    CAMPAIGNS_PAUSE_URL = 'https://api.exoclick.com/v2/campaigns/pause'
    CAMPAIGNS_VARIATION_PUT_URL = 'https://api.exoclick.com/v2/campaigns/{0}/variation/{1}'
    CAMPAIGNS_VARIATION_PALY_URL = 'https://api.exoclick.com/v2/campaigns/{0}/variation/{1}/play'
    CAMPAIGNS_VARIATION_PAUSE_URL = 'https://api.exoclick.com/v2/campaigns/{0}/variation/{1}/pause'
    CAMPAIGNS_SITES_PUT_URL = 'https://api.exoclick.com/v2/campaigns/{0}/{1}/sites'

    # DELETE接口
    LANGUAGES_DELETE_URL = 'https://api0.exoclick.com/v2/campaigns/{0}/targeted/languages/all'
    BROWSERS_DELETE_URL = 'https://api0.exoclick.com/v2/campaigns/{0}/targeted/browsers/all'
    OPERATINGS_SYSTEM_DELETE_URL = 'https://api0.exoclick.com/v2/campaigns/{0}/targeted/operating_systems/all'
    CARRIERS_DELETE_URL = 'https://api0.exoclick.com/v2/campaigns/{0}/targeted/carriers/all'
    DEVICES_DELETE_URL = 'https://api0.exoclick.com/v2/campaigns/{0}/targeted/devices/all'



