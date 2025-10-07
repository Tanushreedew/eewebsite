from django.urls import path
from news import views

urlpatterns = [
    path('create', views.NewsView.as_view()),
    path('read', views.GetNewsView.as_view())
]
