from django.db import models
from django.contrib.auth.models import AbstractUser

from userapp.models import User



class StudentProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recent_research = models.TextField(max_length=150)
    research_abstract = models.TextField(max_length=150)
    scholarship_needed= models.BooleanField(default=False)



    class Meta:

        verbose_name = 'StudentProfile'



