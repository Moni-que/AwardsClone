from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^index',views.index,name='index'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^upload',views.upload,name = "upload"),
    re_path(r'^search/',views.search_results,name='search_results'),
    re_path(r'^profile',views.profile,name = "profile"),
    re_path(r'^add_profile',views.add_profile,name = "add_profile"),
    re_path(r'^update_profile/(\d+)',views.update_profile,name = "update_profile"),
    re_path(r'^profile_id/(\d+)', views.project_details, name="project_details"),
    re_path(r'^review/(\d+)',views.review_project, name='review_project'),
    re_path(r'^project/(\d+)', views.project_details, name="project_details"),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)