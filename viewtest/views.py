from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET请求')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post请求')


class StaticView(View):
    def get(self, request, imgname, *args, **kwargs):
        import re
        filepath = request.path
        m = re.match('/viewtest/(.*)', filepath)
        filename = m.group(1)
        print(filepath)
        print(filename)
        return HttpResponse('GET请求')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post请求')


def showstatic(request):
    return render(request, "showstatic.html")
