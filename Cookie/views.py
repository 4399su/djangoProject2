from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def setCookie(request):
    response = HttpResponse()

    # 默认保存到关闭浏览器
    response.set_cookie('uname', 'uname', max_age=24 * 60 * 60)

    return response
