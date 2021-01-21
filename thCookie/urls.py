from django.urls import path

from thCookie import views

urlpatterns = [
    path('thcookie/', views.thcookie),
]