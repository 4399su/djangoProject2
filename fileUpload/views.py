from django.http import HttpResponse
from django.shortcuts import render
import os


# Create your views here.
def fileUpload(request):
    m = request.method
    if m == 'GET':
        return render(request, "fileUpload.html")
    else:
        uname = request.POST.get("uname", '')
        photo = request.FILES.get("photo", '')
        if not os.path.exists("media"):
            os.mkdir("media")

        with open(os.path.join(os.getcwd(), 'media', photo.name), 'wb') as f:
            f.write(photo.read())

        return HttpResponse("上传成功")
