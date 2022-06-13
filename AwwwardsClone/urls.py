from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^signin',views.signin,name='signin'),
    re_path(r'^logout',views.logout,name='logout'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)