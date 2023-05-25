from django.urls import path

from student import views

urlpatterns = [

    # USER
    path('register-student/', views.StudentRegister),
    path('search-professor-result/', views.SearchProfessorResult),
    path('education-history/', views.UpdateEducationHistory),


]