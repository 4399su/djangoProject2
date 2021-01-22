from django.urls import path

from viewtest import views

urlpatterns = [
    path('thcookie/', views.showview),
]
