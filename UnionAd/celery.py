__author__ = 'cwd'
__date__ = '2018/3/12 10:22'

from celery import Celery
from UnionAd import settings
import os

# 获取当前文件夹名，即为该Django的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '{0}.settings'.format(project_name)

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化Celery
app = Celery(project_name)

# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings')

# Celery加载所有注册的应用
# 如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任务，在django中会实时地检索出来。
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)

