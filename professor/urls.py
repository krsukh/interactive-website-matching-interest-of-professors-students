from django.urls import path

from professor import views

urlpatterns = [

    # USER
    path('register-professor/', views.ProfessorRegister),
    path('search-student/', views.SearchStudent),
    path('professor-education-history/', views.ProfessorEducationHistoryUpdate),

]