from django.urls import path

from retest import views

urlpatterns = [
    path('showre/', views.show),
    path('showre1/', views.showone),
]
