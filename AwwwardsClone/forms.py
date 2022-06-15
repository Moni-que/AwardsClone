from django import forms
from django.db.models import fields
from . models import Project,Profile


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project        
        fields=['image',
                 'user',
                 'project_link',
                 'project_name',
                 'project_description',
        ]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact')    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','contact')  