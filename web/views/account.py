'''
用户账户相关功能存放在这里：注册、短信、登录、注销
'''
from django.shortcuts import render
from web.forms.account import RegisterModleForm
def register(request):
    form=RegisterModleForm()
    return render(request, 'register.html',{'form':form})
