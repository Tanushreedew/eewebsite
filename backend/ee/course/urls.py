from django.urls import path
from course import views

urlpatterns = [
    path('create', views.CreateCourseView.as_view()),
    path('read/<program>', views.GetCourseByProgramView.as_view()),
    path('read/elective/<program>', views.GetElectiveByProgramView.as_view()),
    path('read/<program>/new', views.GetCourseByProgramNewView.as_view()),
]

