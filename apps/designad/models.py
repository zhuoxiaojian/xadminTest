from django.db import models
from datetime import datetime
from users.models import UserProfile
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class GeographicLocation(models.Model):
    id = models.IntegerField(verbose_name='地理位置id', primary_key=True,  default='1')
    short_name = models.CharField(verbose_name='地理位置简称', max_length=128, default='China')
    long_name = models.CharField(verbose_name='地理位置简称', max_length=250, default='China')
    chn_name = models.CharField(verbose_name='地理位置中文名称', max_length=250)
    iso2 = models.CharField(verbose_name='地理位置名称ios2版本', max_length=50, default='ch')
    iso3 = models.CharField(verbose_name='地理位置名称ios3版本', max_length=50, default='ch')

    class Meta:
        verbose_name = '地理位置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chn_name


class Languages(models.Model):
    id = models.IntegerField(verbose_name='语言id', primary_key=True, default='1')
    name = models.CharField(verbose_name='语言名称', max_length=100, default='China')
    chn_name = models.CharField(verbose_name='语言中文名称', max_length=100)
    iso2 = models.CharField(verbose_name='语言名称ios2版本', max_length=50, default='ch')
    iso2_two = models.CharField(verbose_name='语言名称ios2第二版本', max_length=50, default='ch')

    class Meta:
        verbose_name = '语言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Advertise(models.Model):
    name = models.CharField(verbose_name='投放站点', max_length=128, default='投放站点')

    class Meta:
        verbose_name = '投放站点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlocksAds(models.Model):
    name = models.CharField(verbose_name='屏蔽站点', max_length=128, default='屏蔽站点')

    class Meta:
        verbose_name = '屏蔽站点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Categories(models.Model):
    id = models.IntegerField(verbose_name='类别id', primary_key=True,  default='1')
    name = models.CharField(verbose_name='屏蔽站点', max_length=128, default='屏蔽站点')
    parent = models.IntegerField(verbose_name='父级id', default=0)

    class Meta:
        verbose_name = '广告类别'
        verbose_name_plural = verbose_name
        ordering = ['parent']

    def __str__(self):
        return self.name


class Browsers(models.Model):
    id = models.IntegerField(verbose_name='浏览器id', primary_key=True,  default='1')
    name = models.CharField(verbose_name='浏览器名称', max_length=128, default='Internet Explorer')

    class Meta:
        verbose_name = '浏览器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MobileCarriers(models.Model):
    id = models.IntegerField(verbose_name='移动运营商id', primary_key=True,  default='1')
    name = models.CharField(verbose_name='移动运营商名称', max_length=128, default='Internet Explorer')
    country_id = models.IntegerField(verbose_name='国家id', default=1)
    enabled = models.IntegerField(verbose_name='移动运营商可用状态', default=1)

    class Meta:
        verbose_name = '移动运营商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Devices(models.Model):
    id = models.IntegerField(verbose_name='设备id', primary_key=True,  default='1')
    name = models.CharField(verbose_name='设备名称', max_length=128, default='Desktop')

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OperatingSystems(models.Model):
    id = models.IntegerField(verbose_name='操作系统id', primary_key=True,  default='1')
    name = models.CharField(verbose_name='操作系统名称', max_length=128, default='Windows 8.1')
    type = models.IntegerField(verbose_name='操作系统类型', default=0)

    class Meta:
        verbose_name = '操作系统'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Monday(models.Model):
    monTime = models.CharField(verbose_name='星期一时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期一时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.monTime


class Tuesday(models.Model):
    tueTime = models.CharField(verbose_name='星期二时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期二时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tueTime


class Wednesday(models.Model):
    wedTime = models.CharField(verbose_name='星期三时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期三时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.wedTime


class Thursday(models.Model):
    thurTime = models.CharField(verbose_name='星期四时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期四时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.thurTime


class Friday(models.Model):
    friTime = models.CharField(verbose_name='星期五时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期五时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.friTime


class Saturday(models.Model):
    satTime = models.CharField(verbose_name='星期六时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期六时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.satTime


class Sunday(models.Model):
    sunTime = models.CharField(verbose_name='星期日时间', max_length=128, default='8:00')

    class Meta:
        verbose_name = '星期日时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sunTime


# 广告主体
class DesignAdList(models.Model):
    adUser = models.ForeignKey(UserProfile, verbose_name='所属用户', null=True, on_delete=models.CASCADE)
    adName = models.CharField(verbose_name='广告活动名称', max_length=250, default='', help_text='格式推荐：公司-产品')
    # adSite = models.CharField(verbose_name='推广URL', max_length=250, default='http://')
    adStyle = models.CharField(verbose_name='广告样式', max_length=30, default='Banner - 300x250',
                               choices=(
                                   ('Banner - 300x250', '横幅 - 300x250'),
                                   ('Banner - 468x60', '横幅 - 468x60'),
                                   ('Banner - 728x90', '横幅 - 728x90'),
                                   ('Banner - 250x250', '横幅 - 250x250'),
                                   ('Banner - 120x600', '横幅 - 120x600'),
                                   ('Banner - 160x600', '横幅 - 160x600'),
                                   ('Banner - 315x300', '横幅 - 315x300'),
                                   ('Mobile - 300x50', '移动 - 300x50'),
                                   ('Mobile - 300x100', '移动 - 300x100'),
                               ))
    keywords = models.TextField(verbose_name='关键词', default='', help_text='提示：每个关键词请换行分开，请不要输入中文')
    sites = models.TextField(verbose_name='站点目标定位', default='', blank=True, help_text='提示：每个站点请换行分开，在站点前加-号代表屏蔽此站点')

    categoriesList = models.ManyToManyField(Categories, verbose_name='广告类别', blank=True)
    geographicLocationList = models.ManyToManyField(GeographicLocation, verbose_name='地理位置', blank=True)

    adAllLanguages = models.BooleanField(default=False, verbose_name="选择全部语言", help_text='提示：选择了此处，则以下语言不用再选择')
    languagesList = models.ManyToManyField(Languages, verbose_name='语言', blank=True)
    adAllBrowsers = models.BooleanField(default=True, verbose_name="选择全部浏览器", help_text='提示：选择了此处，则以下浏览器不用再选择，默认为全选（推荐）')
    browsersList = models.ManyToManyField(Browsers, verbose_name='浏览器', blank=True)
    adAllOperatingSystem = models.BooleanField(default=True, verbose_name="选择全部操作系统", help_text='提示：选择了此处，则以下操作系统不用再选择，默认为全选（推荐）')
    operatingSystemList = models.ManyToManyField(OperatingSystems, verbose_name='操作系统', blank=True)
    adAllMobileCarriers = models.BooleanField(default=True, verbose_name="选择全部移动运营商", help_text='提示：选择了此处，则以下移动运营商不用再选择，默认为全选（推荐）')
    mobileCarriersList = models.ManyToManyField(MobileCarriers, verbose_name='移动运营商', blank=True)
    adAllDevices = models.BooleanField(default=True, verbose_name="选择全部设备", help_text='提示：选择了此处，则以下设备不用再选择，默认为全选（推荐）')
    devicesList = models.ManyToManyField(Devices, verbose_name='设备', blank=True)

    priceModel = models.CharField(verbose_name='价格模式', default='1', max_length=20,
                                       choices=(
                                           ('1', 'CPC'),
                                           ('2', 'CPM'),
                                           ('4', 'Smart CPM'),
                                           ('5', 'CPV'),
                                       ),
                                  help_text='此价格模式在创建广告活动之后将不能再更改，请慎选'
                                  )
    price = models.DecimalField(verbose_name='价格', default='0.10', max_digits=10, decimal_places=2, help_text='CPC模式的价格不能超过1.66', validators=[MinValueValidator(0.00)])
    isMaxDailyBudget = models.BooleanField(verbose_name='设置日均预算上限', default=True, help_text='提示：选择了此处，下面设置的日均预算上限数值才会生效。若不选择此处则日均预算上限默认是无限')
    maxDailyBudget = models.DecimalField(verbose_name='日均预算上限', max_digits=10, decimal_places=2, default=100.00,
                                         validators=[MaxValueValidator(2000), MinValueValidator(100)])

    impressionsEnabled = models.BooleanField(verbose_name='显示频率', max_length=30, default=False, help_text='提示：只有当价格模式是CPM时才需要开启，用以限制一个重复的访问者在一定时间内看到您的广告的次数',
                                  choices=(
                                      (True, '开启'),
                                      (False, '关闭'),
                                  ))
    impressions = models.IntegerField(verbose_name='展现量', default=0, blank=True, help_text='提示：此项为设置重复访问者在一定时间内显示的次数，只有当价格模式是CPM时并选择了“显示频率”中的“开启”后才能生效')

    minutes = models.IntegerField(verbose_name='分钟', default=0, blank=True, help_text='提示：此项为设置重复访问者显示频率的时间（分钟），只有当价格模式是CPM时并选择了“显示频率”中的“开启”后才能生效')

    addAllSite = models.BooleanField(default=True, verbose_name='投放全部站点', help_text='提示：默认投放全部站点')
    # advertiseList = models.ManyToManyField(Advertise, verbose_name='投放站点', blank=True, help_text='默认投放全部站点')
    # blocksAdsList = models.ManyToManyField(BlocksAds, verbose_name='屏蔽站点', blank=True)

    adAllTime = models.BooleanField(default=False, verbose_name="选择全部时间段", help_text='提示：选择了此处，则以下时间不用再选择，每天时间段默认为0:00-0:00，此时间段为一整天')
    mondayList = models.ManyToManyField(Monday, verbose_name='星期一时间', blank=True)
    tuesdayList = models.ManyToManyField(Tuesday, verbose_name='星期二时间', blank=True)
    wednesdayList = models.ManyToManyField(Wednesday, verbose_name='星期三时间', blank=True)
    thursdayList = models.ManyToManyField(Thursday, verbose_name='星期四时间', blank=True)
    fridayList = models.ManyToManyField(Friday, verbose_name='星期五时间', blank=True)
    saturdayList = models.ManyToManyField(Saturday, verbose_name='星期六时间', blank=True)
    sundayList = models.ManyToManyField(Sunday, verbose_name='星期日时间', blank=True)

    campaign_id = models.IntegerField(verbose_name='广告活动ID', default=1, null=True)
    status = models.IntegerField(verbose_name='状态', default=3, null=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    checked = models.IntegerField(verbose_name='是否过审', default='0', null=True)
    isPost = models.IntegerField(verbose_name='是否上传', default='0', null=True)

    class Meta:
        verbose_name = '广告活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adName

    def change_status(self):
        # 如果不mark safe。会对其进行转义
        if self.status == 0 and self.checked == 1:
            return mark_safe("<p style='color:red';>暂停</p>")
        elif self.status == 1 and self.checked == 1:
            return mark_safe("<p style='color:green';>运行中</p>")
        elif self.status == 3 and self.checked == 0:
            return mark_safe("<p style='color:blue';>待审</p>")
        elif self.status == 0 and self.checked == 0:
            return mark_safe("<p style='color:blue';>待审</p>")
        elif self.status == 1 and self.checked == 0:
            return mark_safe("<p style='color:blue';>待审</p>")
        elif self.status == 1 and self.checked == -1:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 0 and self.checked == -1:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 4 and self.checked == 0:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 4 and self.checked == 1:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 4 and self.checked == -1:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 5 and self.checked == 0:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 5 and self.checked == 1:
            return mark_safe("<p style='color:red';>未过审</p>")
        elif self.status == 5 and self.checked == -1:
            return mark_safe("<p style='color:red';>未过审</p>")


    change_status.short_description = "状态"

    def change_button(self):
        if self.status == 0:
            return mark_safe('<input id="start" type="button" data-toggle="modal" data-target="#playModal" class="btn btn-primary" onclick="startCampaign('+str(self.campaign_id)+')" value="运&nbsp;&nbsp;&nbsp;&nbsp;行">')
        elif self.status == 1:
            return mark_safe('<input id="stop" type="button" data-toggle="modal" data-target="#pauseModal" class="btn btn-danger" onclick="stopCampaign('+str(self.campaign_id)+')" value="暂&nbsp;&nbsp;&nbsp;&nbsp;停">')
        elif self.status == 3:
            return mark_safe('<input id="stop" type="button" class="btn btn-info" onclick="#" value="待审中">')
        elif self.status == 4:
            return mark_safe('<input id="stop" type="button" class="btn btn-danger" onclick="#" value="未过审">')
        elif self.status == 5:
            return mark_safe('<input id="stop" type="button" class="btn btn-danger" onclick="#" value="未过审">')

        pass

    change_button.short_description = "操作"


class AdVariation(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户', null=True, blank=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='广告内容名称', max_length=250, default='', null=True,)
    description = models.CharField(verbose_name='广告内容简介', max_length=250,  null=True, blank=True)
    url = models.CharField(verbose_name='推广URL', max_length=250, default='http://', help_text='请输入与上面推广URL相同的URL')
    status = models.IntegerField(verbose_name='状态', blank=True, default='3')
    id_library_file = models.IntegerField(verbose_name='广告创意ID', default='1')
    varId = models.IntegerField(verbose_name='广告内容ID', blank=True, default='1')
    vari_url = models.CharField(verbose_name='创意URL', max_length=250, default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, verbose_name='广告内容添加时间')

    class Meta:
        verbose_name = '广告内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def vari_file(self):
        file_url = self.vari_url
        print(file_url)
        return mark_safe('<img src="/media/'+file_url+'" height=50% width=50%/>')

    vari_file.short_description = "广告创意"

    def change_status(self):
        # 如果不mark safe。会对其进行转义
        if self.status == 0:
            return mark_safe("<p style='color:red';>暂停</p>")
        elif self.status == 1:
            return mark_safe("<p style='color:green';>运行中</p>")
        elif self.status == 3:
            return mark_safe("<p style='color:blue';>待审</p>")

    change_status.short_description = "状态"

    def change_button(self):
        if self.status == 0:
            return mark_safe('<input id="startVar" type="button" class="btn btn-primary" data-toggle="modal" data-target="#playModal" onclick="startVariation('+str(DesignAdList.objects.get(id=self.adCampaigns_id).campaign_id)+','+str(self.varId)+')" value="运&nbsp;&nbsp;&nbsp;&nbsp;行">')
        elif self.status == 1:
            return mark_safe('<input id="stopVar" type="button" class="btn btn-danger" data-toggle="modal" data-target="#pauseModal" onclick="stopVariation('+str(DesignAdList.objects.get(id=self.adCampaigns_id).campaign_id)+','+str(self.varId)+')" value="暂&nbsp;&nbsp;&nbsp;&nbsp;停">')
        elif self.status == 3:
            return mark_safe('<input id="pending" type="button" class="btn btn-info" onclick="#" value="待审中">')
        pass

    change_button.short_description = "操作"


class AdCreative(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户', null=True, blank=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, blank=True, on_delete=models.CASCADE)
    id_library_file = models.IntegerField(verbose_name='广告创意ID', default='1')
    varId = models.IntegerField(verbose_name='广告内容ID', blank=True, default='1')
    created_at = models.DateTimeField(default=datetime.now, blank=True, verbose_name='广告内容添加时间')

    class Meta:
        verbose_name = '广告创意'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adCampaigns.adName


class AdUrl(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户', null=True, blank=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(verbose_name='推广URL', max_length=250, default='http://')
    varId = models.IntegerField(verbose_name='广告内容ID', blank=True, default='1')
    created_at = models.DateTimeField(default=datetime.now, blank=True, verbose_name='广告内容添加时间')

    class Meta:
        verbose_name = '推广URL'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adCampaigns.adName


class AdvertiserAdType(models.Model):
    id = models.IntegerField(verbose_name='广告类型id', primary_key=True, default='1')
    name = models.CharField(verbose_name='广告类型名称', max_length=150, default='')
    media_storage_templates = models.CharField(verbose_name='广告类型', max_length=250, default='')

    class Meta:
        verbose_name = '广告类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 上传文件类
class UserAdFileLibrary(models.Model):
    user = models.ForeignKey(UserProfile,  verbose_name='所属用户', null=True, on_delete=models.CASCADE)
    adMaterial = models.FileField(upload_to='designad/%Y/%m', verbose_name='广告素材', default='',
                                  help_text='提示：上传的广告创意的尺寸大小有：300x250、468x60、728x90、250x250、120x600、160x600、315x300、300x50、300x100（格式：宽x高），否则影响推广效果，可上传jpg、png、gif格式,gif图的动画速度不能太快，否则此广告会审核不过')
    file_name = models.CharField(verbose_name='创意名称', max_length=250, default='')
    file_id = models.BigIntegerField(verbose_name='创意id', default='1')
    type = models.CharField(verbose_name='创意类型', max_length=50, default='')
    width = models.CharField(verbose_name='创意的宽', max_length=50, default='')
    height = models.CharField(verbose_name='创意的高', max_length=50, default='')
    file_extension = models.CharField(verbose_name='创意后缀名', max_length=50, default='')
    file_size = models.CharField(verbose_name='创意大小', max_length=50, default='')
    url = models.CharField(verbose_name='创意url', max_length=250, default='')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='创意添加时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='创意更新时间')

    class Meta:
        verbose_name = '广告创意'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_name

    def vari_file(self):
        file_url = self.adMaterial.url
        return mark_safe('<img src="'+file_url+'" height=50% width=50%/>')

    vari_file.short_description = "广告创意"


# 站点统计数据
class SitesData(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,  verbose_name='所属用户', null=True, on_delete=models.CASCADE)
    adCampaigns = models.ForeignKey(DesignAdList, verbose_name='所属广告活动', null=True, blank=True, on_delete=models.DO_NOTHING)
    site_hostname = models.CharField(verbose_name='站点', max_length=250, default='semyes.cn', db_index=True)
    cost = models.FloatField(verbose_name='消费', default='0.00', null=True, db_index=True)
    impressions = models.IntegerField(verbose_name='展现次数', default='0', null=True)
    clicks = models.IntegerField(verbose_name='点击次数', default='0', null=True)
    avgCpc = models.FloatField(verbose_name='Avg_CPC', default='0.00', null=True, db_index=True)
    avgCpm = models.FloatField(verbose_name='Avg_CPM', default='0.00', null=True, db_index=True)
    ctr = models.FloatField(verbose_name='点击率', default='0.00', null=True)
    cpc = models.FloatField(verbose_name='CPC', default='0.00', null=True)
    cpv = models.FloatField(verbose_name='CPV', default='0.00', null=True)
    cpm = models.FloatField(verbose_name='CPM', default='0.00', null=True)
    G1 = models.IntegerField(verbose_name='G1', default=0, null=True)
    ecpa1 = models.FloatField(verbose_name='ecpa1', default=0, null=True, db_index=True)
    G2 = models.IntegerField(verbose_name='G2', default=0, null=True)
    ecpa2 = models.FloatField(verbose_name='ecpa2', default=0, null=True, db_index=True)
    G3 = models.IntegerField(verbose_name='G3', default=0, null=True)
    ecpa3 = models.FloatField(verbose_name='ecpa3', default=0, null=True, db_index=True)
    G4 = models.IntegerField(verbose_name='G4',  default=0, null=True)
    ecpa4 = models.FloatField(verbose_name='ecpa4', default=0, null=True, db_index=True)
    deliveryRate = models.FloatField(verbose_name='初始消费', max_length=50, default='0.00', null=True, db_index=True)
    date = models.DateField(verbose_name='消费时间', max_length=50, default=datetime.now, null=True)

    class Meta:
        verbose_name = '站点统计数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


# Goal数据
class AdGoals(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='所属用户', null=True, on_delete=models.CASCADE)
    goalId = models.CharField(verbose_name='goal的ID', max_length=250, default='0', null=True)
    idUser = models.CharField(verbose_name='用户ID', max_length=250, default='0', null=True)
    name = models.CharField(verbose_name='goal名称', max_length=250, default='0', null=True)
    seq = models.CharField(verbose_name='goal的序列id', max_length=250, default='0', null=True)
    order = models.IntegerField(verbose_name='顺序',  default=1,
                                       choices=(
                                           (1, 1),
                                           (2, 2),
                                           (3, 3),
                                           (4, 4),
                                           (5, 5),
                                           (6, 6),
                                           (7, 7),
                                           (8, 8),
                                           (9, 9),
                                           (10, 10),
                                       ))
    coa = models.CharField(verbose_name='成本(可选)', max_length=250, default='0', null=True, blank=True)
    goalScript = models.TextField(verbose_name='追踪代码', max_length=250, default='0', null=True)

    class Meta:
        verbose_name = '目标追踪代码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DesignAdSite(DesignAdList):
    class Meta:
        verbose_name = "站点目标定位"
        verbose_name_plural = verbose_name
        proxy = True