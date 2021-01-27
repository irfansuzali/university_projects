from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    school = models.CharField(max_length = 255)

    #Enrollment/Graduation Year
    YEARS = []
    for i in range(-10,10,1):
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
        ('--SELECT--','--SELECT--'),
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    year_in_school = models.CharField(
        max_length=255,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='',
    )

class School(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    class Meta:
        verbose_name_plural = "schools"

    def __str__(self):
        return self.name
    