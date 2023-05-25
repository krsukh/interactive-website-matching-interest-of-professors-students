from django.db import models
from userapp.models import User


degree_offered_choices=[
                            ("Master by Research", 'Master by Research'),
                            ("Phd", 'Phd'),
                            ("Post Doctorate", 'Post Doctorate'),
]

preferred_country_choices = [
    ("USA", 'USA'),
    ("CANADA", 'Canada'),
    ("UK", 'UK'),
    ("INDIA", 'India'),
    ("GERMANY", 'Germany'),
    ("FRANCE", 'France'),
    ("AUSTRALIA", 'Australia'),
]

class ProfessorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_offered = models.CharField(max_length=255, choices=degree_offered_choices,)
    scholarship_provided=models.BooleanField(default=False)
    minimum_qualification_required = models.CharField(max_length=30)
    latest_research_description = models.TextField(max_length=150)
    minimum_gpa_required=models.TextField(max_length=5,null=True,blank=True)
    is_domestic_student=models.BooleanField(default=True)
    is_accepting_international_students=models.BooleanField(default=False)
    home_page_link=models.URLField(max_length=255,null=True,blank=True)
    preferred_country=models.CharField(max_length=255,null=True,blank=True, choices=preferred_country_choices,)


    class Meta:

        verbose_name = 'ProfessorProfile'


