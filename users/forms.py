from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'school_name','year_in_school','enrollment_year','graduation_year')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'school_name','year_in_school','enrollment_year','graduation_year')
        
