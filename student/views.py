from django.http import HttpResponse

from professor.models import ProfessorProfile
from userapp.models import User, Education, MultipleSelectPreferredStudyDestination
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .models import StudentProfile


import spacy

def StudentRegister(request):
    if request.method == 'POST':
        print("cvvvf")
        username = request.POST["username"]
        email = request.POST["email"]
        if User.objects.filter(username=username).exists():
            print("user exists")
            exists_username=True
        if User.objects.filter(email=email).exists():
            print("email exists")
            exists_email = True
        else:
            password = request.POST["password"]
            create_user_student = User.objects.create(first_name=request.POST["first_name"],
                                                      last_name=request.POST["last_name"],
                                                      username=request.POST["username"],
                                                      email=request.POST["email"],
                                                      phone_number=request.POST["phone_number"],
                                                      domestic_country=request.POST["domestic_country"],
                                                      is_student=True)
            create_user_student.set_password(password)
            create_user_student.save()
            print(create_user_student)

            print(request.POST.getlist('preferred_study_destination'), "request.POST.getlist('preferred_study_destination')")
            for d in request.POST.getlist('preferred_study_destination'):
                print(d)
                MultipleSelectPreferredStudyDestination.objects.create(user_id=create_user_student.pk,preferred_study_destination=d)

            try:
                print(1)
                data=request.request.POST.getlist('country_of_education')
                print(data)
                data1=request.POST.getlist('university')
                for a in request.POST.getlist('country_of_education'):
                    print(f"a {a}")
                for b in request.POST.getlist('university'):
                    print(f"b {b}")
                for c in request.POST.getlist('department'):
                    print(f"c {c}")
                for d in request.POST.getlist('specialization'):
                    print(f"d {d}")
                for e in request.POST.getlist('degree_level'):
                    print(f"e {e}")
                for f in request.POST.getlist('degree_name'):
                    print(f"f {f}")
                for g in request.POST.getlist('course_start_date'):
                    print(f"g {g}")
                for h in request.POST.getlist('completion_date'):
                    print(f"h {h}")
                for i in request.POST.getlist('gpa'):
                    print(f"i {i}")

            except:
                try:
                    print(2)
                    for a in request.POST.getlist('country_of_education'):
                        print(f"a {a}")
                    for b in request.POST.getlist('university'):
                        print(f"b {b}")
                    for c in request.POST.getlist('department'):
                        print(f"c {c}")
                    for d in request.POST.getlist('specialization'):
                        print(f"d {d}")
                    for e in request.POST.getlist('degree_level'):
                        print(f"e {e}")
                    for f in request.POST.getlist('degree_name'):
                        print(f"f {f}")
                    for g in request.POST.getlist('course_start_date'):
                        print(f"g {g}")
                    for h in request.POST.getlist('completion_date'):
                        print(f"h {h}")
                    for i in request.POST.getlist('gpa'):
                        print(f"i {i}")

                except:
                    print(3)
                    pass

            #
            Education.objects.create(user=create_user_student,
                                     country_of_education=request.POST['country_of_education'],
                                     university=request.POST["university"],
                                     department=request.POST["department"],
                                     specialization=request.POST["specialization"],
                                     degree_level=request.POST["degree_level"],
                                     degree_name=request.POST["degree_name"],
                                     course_start_date=request.POST["course_start_date"],
                                     completion_date=request.POST["completion_date"],
                                     gpa=request.POST["gpa"])


            print(f"get {request.POST.get('scholarship_needed')}")

            StudentProfile.objects.create(user=create_user_student,
                                          recent_research=request.POST["recent_research"],
                                          research_abstract=request.POST["research_abstract"],
                                          scholarship_needed=request.POST.get("scholarship_needed"))
            studentRegister = True
            return render(request, "loginapp/login.html", locals())
    else:
            return render(request, "student/register-student.html", locals())
    return render(request, "student/register-student.html", locals())


def SearchProfessorResult(request):


    print(request.user)
    user_dept = Education.objects.filter(user=request.user).first()
    print(f"{user_dept}")
    print(f"welcome{user_dept.course_start_date}")

    scholarship = StudentProfile.objects.filter(user=request.user).first()
    print(f"{scholarship}")
    doc=(scholarship.research_abstract)
    print(doc)
    custom_list= list()
    data_list=list()
    highest_nlp_data=list()
    multiple_preferred_country=MultipleSelectPreferredStudyDestination.objects.filter(user=request.user)
    for value in  multiple_preferred_country:
        country=value.preferred_study_destination
        print(f"{country}")
        preferredcountry = ProfessorProfile.objects.filter(preferred_country=country)
        for data in preferredcountry:
            print(f"{data.preferred_country}")


        for country_data in preferredcountry:
            single_user = User.objects.filter(pk=country_data.user.pk).first()
            department_data = Education.objects.filter(user=single_user, department=user_dept.department)
            for single_department in department_data:
                print(f" department {single_department.department}")
                print(f" user {single_department.user.first_name}")
            for qualification in department_data:
                single_user1 = User.objects.filter(pk=single_department.user.pk).first()
                qualification_data=ProfessorProfile.objects.filter(user=single_user1,minimum_qualification_required=user_dept.degree_level)
                for single_qualification in qualification_data:
                    print(f" qualification {single_qualification.minimum_qualification_required}")
                    print(f" user {single_qualification.user.first_name}")
                for gpa in qualification_data:
                    single_user2=User.objects.filter(pk=single_qualification.user.pk).first()
                    gpa_data = ProfessorProfile.objects.filter(user=single_user2,minimum_gpa_required=user_dept.gpa)
                    # print(education_data2)
                    for single_gpa in gpa_data:
                        print(f" gpa {single_gpa.minimum_gpa_required}")
                        print(f" user {single_gpa.user.first_name}")
                    for scholarshipvalue in gpa_data:
                        single_user3 = User.objects.filter(pk=single_gpa.user.pk).first()
                        scholarship_data = ProfessorProfile.objects.filter(user=single_user3,scholarship_provided=scholarship.scholarship_needed)
                        for single_scholarship in scholarship_data:
                            print(f" scholarship {single_scholarship.scholarship_provided}")
                            print(f" user {single_scholarship.user.first_name}")

                        for startdate in scholarship_data:
                            single_user4 = User.objects.filter(pk=single_scholarship.user.pk).first()
                            print(f"userdate{single_user4}")

                            course_date_data = Education.objects.filter(user=single_user4,course_start_date=user_dept.course_start_date)
                            print(course_date_data)
                            for single_course in course_date_data:
                                print(f" course_date {single_course.course_start_date}")
                                print(f" user {single_course.user}")
                                custom_dict = dict()
                                data_dict=dict()
                                custom_dict['username']=single_course.user.first_name
                                data_dict['username']=single_course.user.first_name
                                home_link_data=ProfessorProfile.objects.filter(user=single_user4)
                                for i in  home_link_data:
                                    custom_dict['link']=i.home_page_link
                                    data=(i.latest_research_description)
                                    # print(data)
                                    nlp = spacy.load("en_core_web_sm")
                                    doc1 = nlp(doc)
                                    doc2=nlp(data)
                                    nlp_value=(doc1.similarity(doc2))
                                    # print(nlp_value)
                                    data_dict['data']=nlp_value
                                    data_dict['home_link']=i.home_page_link
                                    custom_dict['link'] = i.home_page_link
                                    data = (i.latest_research_description)
                                    # print(data)
                                    data_list.append(data_dict)
                                    custom_list.append(custom_dict)
                                    # nlp = spacy.load("en_core_web_lg")


    print(data_list)
    maxdata = max(data_list, key=lambda x: x['data'])
    print(f"mamium_data{maxdata}")
    highest_nlp_data.append(maxdata)
    print(highest_nlp_data)


    print(custom_list)
                        # custom_list=custom_list

    return render(request,"student/search_professor_result.html",locals())

def UpdateEducationHistory(request):
    value = Education.objects.filter(user=request.user)
    print(value)
    for i in value:
        print(i.id)

    if request.method=="POST":
        if 'add_new_education' in request.POST:
            print(f"add new ")
            Education.objects.create(user=request.user,
                                     country_of_education=request.POST['country_of_education'],
                                     university=request.POST["university"],
                                     department=request.POST["department"],
                                     specialization=request.POST["specialization"],
                                     degree_level=request.POST["degree_level"],
                                     degree_name=request.POST["degree_name"],
                                     course_start_date=request.POST["course_start_date"],
                                     completion_date=request.POST["completion_date"],
                                     gpa=request.POST["gpa"])
            print(f"added")
        else:
            for i in value:
                print(i)
                update_button=f"update_{i.pk}"
                print(f"update_button 1 {update_button}")
                if update_button in request.POST:
                    print("hello")
                    id=request.POST[f"updateId_{i.pk}"]
                    education=Education.objects.get(id=id)
                    education.university=request.POST[f"university_{i.pk}"]
                    education.degree_name=request.POST[f"degree_name_{i.pk}"]
                    education.specialization=request.POST[f"specialization_{i.pk}"]
                    education.save()
                    updated = True
                    # print(f" pk = {i.pk}")
                    # print(request.POST[f"gpa_{i.pk}"])
                    # print(f" update_button {update_button}")
                    # print(f"update ")
    # value = Education.objects.filter(user=request.user)

    return render(request, "student/update_student_education_history.html", locals())

