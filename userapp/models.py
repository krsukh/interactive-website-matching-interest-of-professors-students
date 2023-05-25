from django.contrib.auth.models import AbstractUser
from django.db import models

domestic_country_choices = [
    ("USA", 'USA'),
    ("CANADA", 'Canada'),
    ("UK", 'UK'),
    ("INDIA", 'India'),
    ("GERMANY", 'Germany'),
    ("FRANCE", 'France'),
    ("AUSTRALIA", 'Australia'),
]

preferred_study_destination_choices = [
    ("USA", 'USA'),
    ("CANADA", 'Canada'),
    ("UK", 'UK'),
    ("INDIA", 'India'),
    ("GERMANY", 'Germany'),
    ("FRANCE", 'France'),
    ("AUSTRALIA", 'Australia'),
]



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    domestic_country = models.CharField(max_length=255, choices=domestic_country_choices, )

class MultipleSelectPreferredStudyDestination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='multiple_preferred_study_destination')
    preferred_study_destination = models.CharField(max_length=255,null=True,blank=True,choices=preferred_study_destination_choices, )


country_of_education_choices=[
                                    ("USA",'USA'),
                                    ("CANADA",'Canada'),
                                    ("UK",'UK'),
                                    ("INDIA",'India'),
                                    ("GERMANY",'Germany'),
                                    ("FRANCE",'France'),
                                    ("AUSTRALIA",'Australia'),
                    ]

university_choices=[
                                    ("Massachusetts Institute of Technology (MIT)",'Massachusetts Institute of Technology (MIT)'),
                                    ("University of Oxford",'University of Oxford'),
                                    ("University of Chicago",'University of Chicago'),
                                    ("University of Toronto",'University of Toronto'),
                                    ("Ruprecht-Karls-Universitat Heidelberg",'Ruprecht-Karls-Universitat Heidelberg'),
                                    ("Monash University",'Monash University'),
                                    ("University of Delhi",'University of Delhi'),
                                    ("Lovely Professional University",'Lovely Professional University'),
                    ]
department_choices=[
                                    ("BCA",'BCA'),
                                    ("Bsc",'Bsc'),
                                    ("BTech",'BTech'),
                                    ("MCA",'MCA'),
                                    ("MSc",'MSc'),
                                    ("MTech",'MTech'),
                                    ("IT",'IT'),
                    ]
specialization_choices=[
                                    ("Analytical Chemistry",'Analytical Chemistry'),
                                    ("Organic Chemistry",'Organic Chemistry'),
                                    ("Biotechnology",'Biotechnology'),
                                    ("Materials & Textiles",'Materials & Textiles'),
                                    ("Technical Support",'Technical Support'),
                                    ("Technical Communication/Science Writing",'Technical Communication/Science Writing'),
                                    ("Human Resources",'Human Resources'),
                    ]
level_of_degree_choices=[
                                    ("Diploma",'Diploma'),
                                    ("Bachelor",'Bachelor'),
                                    ("Post Graduate",'Post Graduate'),
                                    ("Masters",'Masters'),

]

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='education')
    country_of_education = models.CharField(max_length=255, choices=country_of_education_choices,null=True,blank=True )
    university = models.CharField(max_length=255, choices=university_choices, )
    department = models.CharField(max_length=255, choices=department_choices, )
    specialization = models.CharField(max_length=255, choices=specialization_choices, )
    degree_level = models.CharField(max_length=255, choices=level_of_degree_choices,null=True,blank=True )
    degree_name = models.CharField(max_length=50, null=True, blank=True)
    research_lab= models.TextField(max_length=5,null=True,blank=True)
    course_start_date = models.DateField()
    completion_date = models.DateField(null=True,blank= True)
    gpa = models.TextField(max_length=5)

    class Meta:
        verbose_name = 'Education'