from django.urls import path
from events import views

urlpatterns = [
    path('create', views.EventViews.as_view()),
    path('read', views.GetEventView.as_view())
]
