__author__ = 'cwd'
__date__ = '2018/3/7 11:20'
import requests
import json
from utils.CacheUtils import write_to_cache, read_from_cache
import time


class TokenUtils(object):

    def getAPIToken(username, password):
        headers = {
            'Content-Type': 'application/json'
        }

        params = {'username': username, 'password': password}  # 这里账号密码就是抓包的数据
        login_url = 'https://api.exoclick.com/v2/login'
        params = json.dumps(params)
        print(params)

        try:
            r = requests.post(login_url, params, headers)
            print(r.status_code)
            if r.status_code == 200:
                res = eval(r.text)
                write_to_cache(username, res['token'])
                write_to_cache('userTokenType', res['type'])
                print(username)
                print(username+'的token:' + read_from_cache(username))
                print('userTokenType:' + read_from_cache('userTokenType'))
                print('expires_in:' + str(res['expires_in']))

        except requests.exceptions.ConnectionError:
            print("token过期，服务器拒绝链接...")
            print("正在重新链接...")
            TokenUtils.getAPIToken(username, password)


