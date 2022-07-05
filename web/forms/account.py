# 注册功能
from django import forms
from web import models

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