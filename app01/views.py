from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings
# Create your views here.
def send_sms(request):
    '''
    发送短信
    根据用户操作不同
    模板id也就不同
    登录 login  1420060
    注册 register 1420059
    '''
    tpl=request.GET.get('tpl')
    template_id=settings.TENCENT_TEMPLATE.get(tpl)
    # template_id="1400629890"
    if not template_id:
        return HttpResponse('模板不存在')
    code=random.randrange(1000,9999)
    res=send_sms_single('13030650891',template_id,[code,])
    print(res)
    if res['result']==0:
        return HttpResponse('发送成功')
    else:

        return HttpResponse(res['errmsg'])


# 注册功能
from django import forms
from app01 import models

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class RegisterModleForm(forms.ModelForm):

    # 此处可以对表单中的字段进行重写，比如手机号要遵循手机格式，添加正则表达式
    mobile_phone=forms.CharField(label='手机号',validators=[RegexValidator(r'^1[3|4、5|6|7\8|9])\d{9}$','手机号格式错误'),])
    # 把密码隐藏掉
    password= forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))
    # 再次输入密码
    confirm_password=forms.CharField(label='再次输入密码',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请确认密码'}))
    # 添加验证码
    code=forms.CharField(label='验证码',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入密码'}))

    class Meta:
        model=models.UserInfo
        fields=['username','email','password','confirm_password','mobile_phone','code']
    def __init__(self,*args,**kwargs): #c
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():  #name是字段  field是内容
            field.widget.attrs['class']='form-control'  #改变样式
            field.widget.attrs['placeholder']='请输入%s'%(field.label)

def register(request):
    form=RegisterModleForm()
    return render(request, 'web/../web/templates/register.html', {'form':form})
import redis
conn=redis.Redis(host='192.168.127.1',port='6379',encoding='utf-8')
conn.set('13030650891',9999,ex=60)
value=conn.get('13030650891')
print(value)