from django.urls import path, include

from Cookie import views

urlpatterns = [
    path('cookie/', views.setCookie),
    path('cookie/getcookie/', views.getCookie),
]
