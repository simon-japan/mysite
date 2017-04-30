from django.conf.urls import url

from . import views

app_name = 'todo_app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.TodoView.as_view(), name='todo'),
    url(r'^create_todo/(?P<project_id>[0-9]+)/create_todo/$', views.create_todo, name='create_todo')
]