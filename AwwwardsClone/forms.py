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
