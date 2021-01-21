from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def thcookie(request):
    m = request.method
    if m == 'GET':
        if 'login' in request.COOKIES:
            # str = request.COOKIES.get("login").split(',')
            str = request.get_signed_cookie('login', salt='sad').split(',')
            uname = str[0]
            pwd = str[1]
            return render(request, "thcookie.html", {"uname": uname, "pwd": pwd})
        else:
            return render(request, "thcookie.html")
    else:
        response = HttpResponse()
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        ch = request.POST.get('ch')
        if uname == 'abc' and pwd == '123':
            response.content = "登陆成功"
            # response.set_cookie("login", uname + ',' + pwd, path='/thcookie/', max_age=24 * 60 * 60)

            response.set_signed_cookie("login", uname + ',' + pwd, salt='sad', path='/thcookie/', max_age=24 * 60 * 60)
            return response
        else:
            response.content = "登陆失败"

            response.delete_cookie('login', path='/thcookie/')
            return response
