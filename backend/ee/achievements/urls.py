from django.urls import path
from achievements import views

urlpatterns = [
    path('books/read', views.GetBooksAPI.as_view()),
    path('students/read', views.GetStudentAwardsAPI.as_view()),
    path('faculty/read', views.GetFacultyAwardsAPI.as_view()),
    path('patent/read', views.GetPatentAPI.as_view()),
]
