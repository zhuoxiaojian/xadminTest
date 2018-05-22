from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='用户名', unique=True, default='普通用户')
    phone = models.CharField(max_length=11, verbose_name='手机', default='', blank=True)
    exo_name = models.CharField(max_length=150, verbose_name='exo用户名', default='用户')
    exo_password = models.CharField(max_length=150, verbose_name='exo密码', default='')
    exo_id = models.CharField(max_length=150, verbose_name='exo用户ID', default='', blank=True)
    contact = models.CharField(max_length=100, verbose_name='联系人', default='', blank=True)
    tel = models.CharField(max_length=30, verbose_name='电话', default='11111111', null=True, blank=True)
    qq = models.CharField(max_length=30, verbose_name='QQ', default='', null=True, blank=True)

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class AdPriceRate(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    deliveryRate = models.DecimalField(verbose_name='投放率', default=0.10, max_digits=10, decimal_places=2,
                                       validators=[MaxValueValidator(0.90), MinValueValidator(0.10)],
                                       help_text='输入的投放率必须在0.1到0.9之间'
                                       )
    created_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '设置用户投放率'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class RechargeRecord(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    recharge = models.DecimalField(verbose_name='用户充值金额', default=0.00, max_digits=10, decimal_places=2)
    exo_recharge = models.DecimalField(verbose_name='EXO充值金额', default=0.00, max_digits=10, decimal_places=2)
    recharge_deliveryRate = models.DecimalField(verbose_name='本次充值时的投放率', default=0.00, max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户充值记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class UserAcount(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='余额', max_digits=10, decimal_places=2)
    dailyCost = models.FloatField(verbose_name='今日消费金额', default=0.00, null=True)
    monthCost = models.FloatField(verbose_name='本月消费金额', default=0.00, null=True)
    recharge_balance = models.DecimalField(verbose_name='本次充值时EXO的余额', default=0.00, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = '用户消费余额信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')), verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间') #now后不带括号，时间才会根据class实例化的时候生成时间，不去掉括号，时间会根据model编译的时间生成

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code