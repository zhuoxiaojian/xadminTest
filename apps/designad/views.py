import json

from django.http import JsonResponse, HttpResponse
import logging
from django.views.generic import View

# Create your views here.


# 运行广告活动
from designad.models import DesignAdList, AdVariation, UserAdFileLibrary
from utils.Constants import Constants
from utils.HttpUtils import HttpUtils


class AdPlayOrPause(View):
    def get(self, request):
        campaign_id = request.GET.get('id')
        action = request.GET.get('action')
        msg = False
        if action == 'play':
            data = HttpUtils.putHttp(Constants.CAMPAIGNS_PALY_URL, {"campaign_ids": [campaign_id]}, DesignAdList.objects.filter(campaign_id=campaign_id)[0].adUser_id)
            logging.info(data)
            print(data)
            if not data is None:
                print(data.text)
                logging.info(data.text)
                if data.status_code == 200:
                    DesignAdList.objects.filter(campaign_id=campaign_id).update(status=1)
                    msg = True


        elif action == 'pause':
            data = HttpUtils.putHttp(Constants.CAMPAIGNS_PAUSE_URL, {"campaign_ids": [campaign_id]},
                                     DesignAdList.objects.filter(campaign_id=campaign_id)[0].adUser_id)
            logging.info(data)
            print(data)
            if not data is None:
                logging.info(data.text)
                print(data.text)
                if data.status_code == 200:
                    DesignAdList.objects.filter(campaign_id=campaign_id).update(status=0)
                    msg = True
        return JsonResponse({'success': msg})


class AdVariationPlayOrPause(View):
    def get(self, request):
        campaign_id = request.GET.get('id')
        variation_id = request.GET.get('varId')
        action = request.GET.get('action')
        msg = False
        if action == 'play':
            print(Constants.CAMPAIGNS_VARIATION_PALY_URL.format(campaign_id, variation_id))
            data = HttpUtils.putVarPlayOrPuaseHttp(Constants.CAMPAIGNS_VARIATION_PALY_URL.format(campaign_id, variation_id),
                                                   AdVariation.objects.filter(varId=variation_id)[0].user_id)
            logging.info(data)
            print(data)
            if not data is None:
                print(data.text)
                logging.info(data.text)
                if data.status_code == 200:
                    AdVariation.objects.filter(varId=variation_id).update(status=1)
                    msg = True

        elif action == 'pause':
            print(Constants.CAMPAIGNS_VARIATION_PAUSE_URL.format(campaign_id, variation_id))
            data = HttpUtils.putVarPlayOrPuaseHttp(Constants.CAMPAIGNS_VARIATION_PAUSE_URL.format(campaign_id, variation_id),
                                                   AdVariation.objects.filter(varId=variation_id)[0].user_id)
            logging.info(data)
            print(data)
            if not data is None:
                logging.info(data.text)
                print(data.text)
                if data.status_code == 200:
                    AdVariation.objects.filter(varId=variation_id).update(status=0)
                    msg = True
        return JsonResponse({'success': msg})


class getUserVariation(View):
    def get(self, request):
        print(request.user.id)
        return HttpResponse(json.dumps(list(UserAdFileLibrary.objects.filter(user_id=request.user.id).values('file_id', 'adMaterial', 'width', 'height'))))
