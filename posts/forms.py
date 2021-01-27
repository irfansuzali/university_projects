from django import forms 
from .models import Post,Category


choices = Category.objects.all().values_list('name','name')
choice_list = [('--SELECT--','--SELECT--')]
for item in choices:
    choice_list.append(item)

class CreatePostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title','category','body')
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control' }),
            'category': forms.Select(choices = choice_list, attrs = {'class':'form-control', 'empty_label': 'SELECT'} )
        }