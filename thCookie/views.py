from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def thcookie(request):
    m = request.method
    if m == 'GET':
        if 'login' in request.COOKIES:
            str = request.COOKIES.get("login").split(',')
            uname = str[0]
            pwd = str[1]
        return render(request, "thcookie.html")
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname == 'abc' and pwd == '123':
            response = HttpResponse("登陆成功")
            response.set_cookie("login", uname + ',' + pwd, path='/thcookie/', max_age=24 * 60 * 60)
            return response
        else:
            return HttpResponse("登录失败")
