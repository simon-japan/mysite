from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.project),
    url(r'^todo/(?P<todo_id>[0-9]+)/$', views.todo_detail)
]