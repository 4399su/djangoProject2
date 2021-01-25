# coding=utf-8
from django.urls import path, re_path

from viewtest import views

urlpatterns = [
    path('viewtest/', views.IndexView.as_view()),
    re_path('viewtest/(.*)', views.StaticView.as_view()),
    path('showstatic/',views.showstatic)
]
