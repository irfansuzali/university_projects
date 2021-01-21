from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    #School Name 
    school_name = models.CharField(
        max_length = 500,
        null = True,)

    #Enrollment/Graduation Year
    YEARS = []
    for i in range(0,30,1):
        YEARS.append((2020-i,2020-i))
    
    enrollment_year = models.PositiveSmallIntegerField(
        choices = YEARS,
        default = 2020
    )
    
    graduation_year = models.PositiveSmallIntegerField(
        choices = YEARS,
        default = 2020
    )

    #Current Standing
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='FR',
    )

    