from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def setCookie(request):
    response = HttpResponse()
    import datetime
    # 默认保存到关闭浏览器
    # 默认存储在缓存中，更改存储日期后存储到本地
    # response.set_cookie('uname', 'uname', max_age=24 * 60 * 60,
    #                    expires=datetime.datetime.today() + datetime.timedelta(days=2))

    # 加密
    response.set_signed_cookie('uname', 'uname', salt='dsa', max_age=24 * 60 * 60, path='/cookie/getcookie/')
    return response


def getCookie(request):
    str1 = request.COOKIES.get('uname')
    str = request.get_signed_cookie('uname', salt='dsa')
    return HttpResponse(str)
