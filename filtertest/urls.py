from django.urls import path

from filtertest import views

urlpatterns = [
    path('filter/', views.IndexViews.as_view()),
]