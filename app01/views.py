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
    if not template_id:
        return HttpResponse('模板不存在')
    code=random.randrange(1000,9999)
    res=send_sms_single('17356530931',template_id,[code,])
    print(res)
    if res['result']==0:
        return HttpResponse('发送成功')
    else:

        return HttpResponse(res['errmsg'])