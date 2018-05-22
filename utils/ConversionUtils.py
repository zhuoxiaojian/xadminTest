from users.models import AdPriceRate
from decimal import Decimal

__author__ = 'cwd'
__date__ = '2018/3/28 20:39'

deliveryRate = 0


# 上传到Exo的数据换算
def meToExo(userId, price, date):
    global deliveryRate
    adRate = AdPriceRate.objects.filter(user_id=userId).order_by("-created_time")

    if adRate.count() > 1:
        print('最前一天' + str(adRate[0].created_time))
        for d in adRate:
            if date >= d.created_time:
                print('前一天' + str(d.created_time))
                deliveryRate = d.deliveryRate
                break
    elif adRate.count() == 1:
        print('只有一天' + str(adRate[0].created_time))
        deliveryRate = adRate[0].deliveryRate

    print('上传投放率：' + str(deliveryRate))
    converPrice = float(price) * float(deliveryRate)

    return converPrice


# 从Exo获取的数据换算
def exoToMe(userId, price, date):
    global deliveryRate
    adRate = AdPriceRate.objects.filter(user_id=userId).order_by("-created_time")
    # 汇率和投放率
    if adRate.count() > 1:
        for d in adRate:
            if date >= d.created_time:
                print('前一天' + str(d.created_time))
                deliveryRate = d.deliveryRate
                break
    elif adRate.count() == 1:
        print('只有一天' + str(adRate[0].created_time))
        deliveryRate = adRate[0].deliveryRate
    print('获取数据投放率：' + str(deliveryRate))
    converPrice = (float(price) / float(deliveryRate))

    return converPrice


def getRate(userId, date):
    global deliveryRate
    print('传递过来的时间：'+str(date))
    adRate = AdPriceRate.objects.filter(user_id=userId).order_by("-created_time")
    # 汇率和投放率
    if adRate.count() > 1:
        for d in adRate:
            if date >= d.created_time:
                print('前一天' + str(d.created_time))
                deliveryRate = d.deliveryRate
                break
    elif adRate.count() == 1:
        print('只有一天' + str(adRate[0].created_time))
        deliveryRate = adRate[0].deliveryRate
    print('获取数据投放率：' + str(deliveryRate))
    return {'deliveryRate': deliveryRate}
