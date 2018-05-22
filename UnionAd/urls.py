"""UnionAd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.http import HttpResponse

import xadmin
# 导入x admin，替换admin
from django.views.static import serve
from UnionAd.settings import MEDIA_ROOT#, STATICFILES_DIRS
from designad.views import AdPlayOrPause, AdVariationPlayOrPause, getUserVariation

urlpatterns = [
    url('^admin/', xadmin.site.urls),
    url('^$', RedirectView.as_view(url='/admin'), name='login'),
    # path('refleshAdData/', xadmin.site.urls),
    url('^login/', RedirectView.as_view(url='/admin'), name='login'),
    url('^admin/designad/designadlist/adPlayOrStop', AdPlayOrPause.as_view(), name='adPlayOrStop'),
    url('^admin/designad/advariation/adVarPlayOrPause', AdVariationPlayOrPause.as_view(), name='adVarPlayOrPause'),
    url('^admin/getUserVariation', getUserVariation.as_view(), name='getUserVariation'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url('^captcha/', include('captcha.urls')),
    url('^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /admin', content_type='text/plain')),

]

# 全局 404 500 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'