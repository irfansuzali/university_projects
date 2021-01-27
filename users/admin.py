from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, School

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1', 'password2', 'first_name','last_name', 'email','school','year_in_school','enrollment_year','graduation_year')},

        ),
    )
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','last_name', 'email','school','year_in_school','enrollment_year','graduation_year')},
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(School)