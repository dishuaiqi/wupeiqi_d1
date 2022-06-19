'''
用户账户相关功能存放在这里：注册、短信、登录、注销
'''
from django.shortcuts import render

def register(request):
    return render(request, 'web/../templates/register.html')
