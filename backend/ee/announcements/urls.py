from django.urls import path
from announcements import views

urlpatterns = [
    path('create', views.AnnouncementViews.as_view()),
    path('read',views.GetAnnouncementsView.as_view())
]