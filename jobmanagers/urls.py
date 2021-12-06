from django.urls import path
from jobmanagers import views
urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('jobs/', views.JobList.as_view()),
    path('job/<int:pk>/', views.JobDetail.as_view()),
]