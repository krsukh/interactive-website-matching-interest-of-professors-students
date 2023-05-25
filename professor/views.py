from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from professor.models import ProfessorProfile
from userapp.models import User,Education

def ProfessorRegister(request):

    if request.method=='POST':
        username = request.POST["username"]
        email = request.POST["email"]
        if User.objects.filter(username=username).exists():
            print("user exists")
            professor_username = True
        if User.objects.filter(email=email).exists():
            print("email exists")
            professor_email = True
        else:
          password=request.POST["password"]
          create_user_professor = User.objects.create(first_name=request.POST["first_name"],
                                                    last_name=request.POST["last_name"],
                                                    username=request.POST["username"],
                                                    email=request.POST["email"],
                                                    phone_number=request.POST["phone_number"],
                                                    domestic_country=request.POST["domestic_country"],
                                                    is_professor=True)
          create_user_professor.set_password(password)
          create_user_professor.save()


          y=Education.objects.create(user=create_user_professor,
                                   university= request.POST["university"],
                                   department=request.POST["department"],
                                   specialization=request.POST["specialization"],
                                   course_start_date=request.POST["course_start_date"],
                                   research_lab=request.POST["research_lab"])


          try:
              is_accepting_international_students= request.POST['is_accepting_international_students']

              ProfessorProfile.objects.create(user=create_user_professor,
                                              is_accepting_international_students=True,
                                              home_page_link=request.POST["home_page_link"],
                                              degree_offered=request.POST["degree_offered"],
                                              minimum_gpa_required=request.POST["minimum_gpa_required"],
                                              minimum_qualification_required=request.POST[
                                                  "minimum_qualification_required"],
                                              latest_research_description=request.POST[
                                                  "latest_research_description"],
                                              scholarship_provided=request.POST.get("scholarship_provided"))

              professor = ProfessorProfile.objects.get(user=create_user_professor
                                                       )
              professor.is_domestic_student = False
              professor.preferred_country = request.POST["preferred_country"]
              professor.save()

          except:
                  ProfessorProfile.objects.create(user=create_user_professor ,

                                                      home_page_link=request.POST["home_page_link"],
                                                      degree_offered=request.POST["degree_offered"],
                                                      minimum_gpa_required=request.POST["minimum_gpa_required"],
                                                      minimum_qualification_required=request.POST["minimum_qualification_required"],
                                                      latest_research_description=request.POST["latest_research_description"],
                                                      scholarship_provided=request.POST.get("scholarship_provided"))


          professorRegister = True
          return render(request,"loginapp/login.html",locals())

    else:
        return render(request, "professor/register-professor.html", locals())
    return render(request, "professor/register-professor.html", locals())
def SearchStudent(request):
    return render(request,"professor/search_student.html",locals())



def ProfessorEducationHistoryUpdate(request):
    data=Education.objects.get(user=request.user)
    print('data::', data.id)

    if request.method == "POST":

        data.university = request.POST["university"]
        data.specialization = request.POST["specialization"]
        data.research_lab = request.POST["research_lab"]
        data.save()



    return render(request, "professor/professor_education_history.html", locals())