from django.urls import path

from fileUpload import views

urlpatterns = [
    path('file/', views.fileUpload),
]
