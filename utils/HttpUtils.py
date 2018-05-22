import json

import requests
from urllib3 import request

from users.models import UserProfile

__author__ = 'cwd'
__date__ = '2018/3/7 11:50'
from utils.CacheUtils import read_from_cache, checkKey
from utils.TokenUtils import TokenUtils


class HttpUtils(object):

    def getHeader(isFile, userId):
        print(UserProfile.objects.filter(id=userId)[0].exo_name)
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        # userToken = str(UserProfile.objects.filter(id=userId)[0].exo_name)\
        #             + username
        # print('对应用户：'+username+'   对应token'+read_from_cache(username))
        if not read_from_cache(username) is None:

            if not isFile:
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': read_from_cache('userTokenType') + " " + read_from_cache(username),
                }
            else:
                headers = {
                    'Accept': 'application/json',
                    'Authorization': read_from_cache('userTokenType') + ' ' + read_from_cache(username),
                }
            return headers
        else:
            TokenUtils.getAPIToken(username, password)

    def getHttp(url, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        print('对应用户id:::'+ str(userId) + '::对应用户名:::' + username)
        # print(username+'getHttp相应头部：：' + json.dumps(HttpUtils.getHeader(False, userId)))
        n = requests.get(url=url, headers=HttpUtils.getHeader(False, userId), verify=True)
        print('用户：'+username)
        print(username+'getHttp相应：' + str(n.status_code))
        print(username+'getHttp相应：'+n.text)
        if n.status_code == 200:
            return n
        elif n.status_code == 401:
            print('401getHttp头部：' + read_from_cache('userTokenType'))
            print('401gethttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n

    def postHttp(url, body, isFile, userId):
        print(HttpUtils.getHeader(isFile, userId))
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        if isFile:
            n = requests.post(url=url, files=body, headers=HttpUtils.getHeader(isFile, userId), verify=True)
        else:
            n = requests.post(url=url, json=body, headers=HttpUtils.getHeader(isFile, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print('postHttp头部：' + read_from_cache('userTokenType'))
            print('postHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n

    def putHttp(url, body, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        n = requests.put(url=url, json=body, headers=HttpUtils.getHeader(False, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print(username+'putHttp头部：' + read_from_cache('userTokenType'))
            print(username+'putHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n

    def postSitesHttp(url, body, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        n = requests.post(url=url, data=body, headers=HttpUtils.getHeader(False, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print('postSitesHttp头部：' + read_from_cache('userTokenType'))
            print('postSitesHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n


    def putSitesHttp(url, body, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        n = requests.put(url=url, data=body, headers=HttpUtils.getHeader(False, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print('putSitesHttp头部：' + read_from_cache('userTokenType'))
            print('putSitesHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n

    def postVariationHttp(url, body, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        if checkKey('userTokenType') or checkKey(username):
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'accept': 'application/json',
                'authorization': read_from_cache('userTokenType') + " " + read_from_cache(username),
            }
            n = requests.post(url=url, data=body.encode('utf-8'), headers=headers, verify=True)
            if n.status_code == 200:
                print(n)
                return n
            elif n.status_code == 401:
                # token过期需要重新获取
                print('postVariationHttp头部：' + read_from_cache('userTokenType'))
                print('postVariationHttp头部token：' + read_from_cache(username))
                TokenUtils.getAPIToken(username, password)
            else:
                return n
        else:
            TokenUtils.getAPIToken(username, password)


    def putVariationHttp(url, body, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        if checkKey('userTokenType') or checkKey(username):
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'accept': 'application/json',
                'authorization': read_from_cache('userTokenType') + " " + read_from_cache(username),
            }
            n = requests.post(url=url, data=body.encode('utf-8'), headers=headers, verify=True)
            print(n.status_code)
            print(n.text)
            if n.status_code == 200:
                print(n)
                return n
            elif n.status_code == 401:
                # token过期需要重新获取
                print('putVariationHttp头部：' + read_from_cache('userTokenType'))
                print('putVariationHttp头部token：' + read_from_cache(username))
                TokenUtils.getAPIToken(username, password)
            else:
                return n
        else:
            TokenUtils.getAPIToken(username, password)


    def putVarPlayOrPuaseHttp(url, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        n = requests.put(url=url, data=None, headers=HttpUtils.getHeader(False, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print(username + 'putVarPlayOrPuaseHttp头部：' + read_from_cache('userTokenType'))
            print(username + 'putVarPlayOrPuaseHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n


    def deleteHttp(url, userId):
        # 用户exo信息
        username = UserProfile.objects.filter(id=userId)[0].exo_name
        password = UserProfile.objects.filter(id=userId)[0].exo_password
        n = requests.delete(url=url, headers=HttpUtils.getHeader(False, userId), verify=True)
        if n.status_code == 200:
            print(n)
            return n
        elif n.status_code == 401:
            # token过期需要重新获取
            print(username + 'deleteHttp头部：' + read_from_cache('userTokenType'))
            print(username + 'deleteHttp头部token：' + read_from_cache(username))
            TokenUtils.getAPIToken(username, password)
        else:
            return n
