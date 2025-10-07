from django.urls import path
from research import views

urlpatterns = [
    path('research/create', views.ResearchView.as_view()),
    path('research/read', views.GetResearchView.as_view()),
    path('papers/create', views.PapersView.as_view()),
    path('papers/read', views.GetPapersView.as_view()),
    path('project/create', views.ProjectView.as_view()),
    path('project/read', views.GetProjectView.as_view()),
    path('labs/create', views.LabsView.as_view()),
    path('labs/ug/read', views.GetUGLabsView.as_view()),
    path('labs/pg/read', views.GetPGLabsView.as_view()),
    path('<specialization>', views.GetResearchBySpecialisation.as_view())
]
