from django.urls import path
from people import views

urlpatterns = [
    path('BTech/read/<year>', views.GetBtechByYear.as_view()),
    path('MTech/read/<year>', views.GetMtechByYear.as_view()),
    path('PhD/read/<year>', views.GetPhdByYear.as_view()),
    path('Alumni/read/<year>', views.GetAlumniByYear.as_view()),
    path('Staff/read', views.GetStaffView.as_view()),
    path('Faculty/read', views.GetFacultyView.as_view()),
    path('MS/read/<year>', views.GetMSByYear.as_view()),
]
