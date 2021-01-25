from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexViews(View):
    def get(self, request):
        import datetime
        d = datetime.datetime.today()
        urlstr = '<h3></h3>'
        content ="####自定义过滤器"
        return render(request, "index.html", {"num": 8, "str": "ca", "d": d, "urlstr": urlstr})
