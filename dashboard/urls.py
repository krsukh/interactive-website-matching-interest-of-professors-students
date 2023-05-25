from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.dashboard_index),
    path('student-profile/',views.StudentUpdateProfile),
    path('professor-profile/',views.ProfessorUpdateProfile),
    ]