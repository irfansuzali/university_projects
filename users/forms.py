from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, School

school_choices = School.objects.all().values_list('name','name')
school_list = [('--SELECT--','--SELECT--')]
for school in school_choices:
    school_list.append(school)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','school', 'year_in_school','enrollment_year','graduation_year')
        widgets = {
            'school': forms.Select(choices = school_list, attrs = {'class':'form-control', 'empty_label': 'SELECT'})
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','school','year_in_school','enrollment_year','graduation_year')


    