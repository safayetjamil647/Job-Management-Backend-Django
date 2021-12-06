from django.urls import path
from jobmanagers import views
urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('jobs/', views.JobList.as_view()),
    path('job/<int:pk>/', views.JobDetail.as_view()),
    path('category/',views.CategoryList.as_view()), 
    path('category/<int:pk>/',views.CategoryDetail.as_view()),
    path('tech/',views.TechList.as_view()), 
    path('tech/<int:pk>/',views.TechDetail.as_view()),  
    path('location/<int:pk>/',views.LocationList.as_view()), 
    path('location/',views.LocationDetail.as_view()),  
]