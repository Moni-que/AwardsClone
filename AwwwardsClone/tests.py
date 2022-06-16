from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile

# Create your tests here.
class ProjectTestClass(TestCase):  # Project class test
    def setUp(self):
        # creating a user
        user = User.objects.create(username="testing", first_name="monique", last_name="bambi")

        self.project = Project(project_name="Test Name", project_description="Test Description", user=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)


    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)



class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user", first_name="monique", last_name="bambi")
        self.profile = Profile(bio="Test Bio", user=user, contact="Test Number",)


    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)