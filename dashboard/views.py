from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render

from professor.models import ProfessorProfile
from student.models import StudentProfile
from userapp.models import *


# Create your views here.
def dashboard_index(request):
    if request.user.is_professor:
        professor_tab = True
    elif request.user.is_student:
        student_tab = True
    return render(request, "index.html", locals())




def StudentUpdateProfile(request):
    x=MultipleSelectPreferredStudyDestination.objects.filter(user=request.user.id)
    research=StudentProfile.objects.get(user=request.user)
    scholarship_value=Education.objects.filter(user=request.user.id)
    print(scholarship_value)

    if request.method == "POST":
        request.user.first_name = request.POST["first_name"]
        request.user.last_name = request.POST["last_name"]
        request.user.phone_number = request.POST["phone_number"]
        request.user.save()

        research.recent_research=request.POST["recent_research"]
        research.research_abstract=request.POST["research_abstract"]
        research.save()

        #
        # StudentProfile.objects.update(user=request.user, recent_research=request.POST["recent_research"],research_abstract=request.POST["research_abstract"])
        updated=True
        return render(request, "dashboard/update_profile.html", locals())
    return render(request, "dashboard/update_profile.html",locals())



def ProfessorUpdateProfile(request):
    research=ProfessorProfile.objects.get(user=request.user)
    print(research.id)
    if request.method == "POST":
        request.user.first_name = request.POST["first_name"]
        request.user.last_name = request.POST["last_name"]
        request.user.phone_number = request.POST["phone_number"]
        request.user.save()

        research.latest_research_description=request.POST["latest_research_description"]
        research.save()

        # ProfessorProfile.objects.update(user=request.user,latest_research_description=request.POST["latest_research_description"])
        updated=True
        return render(request, "dashboard/update_professor_profile.html", locals())
    return render(request, "dashboard/update_professor_profile.html",locals())
