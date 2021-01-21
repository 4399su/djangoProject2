from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show(request):
    sc = request.scheme
    body = request.body
    path = request.path

    # 返回字典
    get = request.GET
    post = request.POST

    # 返回请求报文信息
    meta = request.META
    # return HttpResponse('scheme:{%s}  body:{%s}'.format( % sc %body))
    # return HttpResponse(' body:%s' % body)
    return HttpResponse('hello world', content_type='text/plain')


def showone(request):
    return render(request, "showre.html")
