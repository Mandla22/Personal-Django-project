from django.conf.urls import url
from . import views


app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^projects/$', views.projects, name="projects"),
    #download urls
    url(r'^projects/download/(?P<filename>[\w\-\.]+)/$', views.download, name="download"),
]

