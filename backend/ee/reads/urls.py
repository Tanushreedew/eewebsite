from django.urls import path
from reads import views

urlpatterns = [
    path('create', views.CreateReadAPIView.as_view()),
    path('post', views. ReadListAPIView.as_view()),
    path('delete/<id>', views.DeleteAPIView.as_view()),
]
