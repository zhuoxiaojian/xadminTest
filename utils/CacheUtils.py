__author__ = 'cwd'
__date__ = '2018/3/7 10:32'
import json
from django.conf import settings
from django.core.cache import cache


# read cache
def read_from_cache(key):
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data


# write cache
def write_to_cache(key, api_token):
    cache.set(key, json.dumps(api_token), settings.NEVER_REDIS_TIMEOUT)


# write cache
def write_adrecode_to_cache(key, adrecode):
    cache.set(key, json.dumps(adrecode), settings.DAY_REDIS_TIMEOUT)


def checkKey(key):
    return cache.has_key(key)