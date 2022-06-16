from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)


    def save_profile(self):
        self.save() 

   
    def delete_profile(self):
        self.delete()

   
    def _str_(self):
        return self.profile_photo

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="projects")
    image = models.ImageField(upload_to='images')
    project_link = models.URLField(max_length=255)
    project_name = models.CharField(max_length=150)
    project_description = models.TextField(max_length=500)


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

   
  # search project using project name
    @classmethod
    def search_results_name(cls, search_term):
        images = cls.objects.filter(project_name__icontains=search_term)
        return images  

    def str(self):
        return self.project_name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_review = models.IntegerField(default=0, blank=True, null=True)
    usability_review = models.IntegerField(default=0, blank=True, null=True)
    content_review = models.IntegerField(default=0, blank=True, null=True)


    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.user.username