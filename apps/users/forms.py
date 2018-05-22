

# 引入Django表单
from django import forms

# 引入验证码field
from captcha.fields import CaptchaField

# 验证码form
class CaptcharForm(forms.Form):
    # 应用验证码
    captcha = CaptchaField()