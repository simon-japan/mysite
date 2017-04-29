from django.shortcuts import render
from django.http import HttpResponse

from .models import Project
from .models import Todo


def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")


def project(request, project_id):
    p = Project.objects.get(pk=project_id)
    return HttpResponse(p.name)


def todo_detail(request, todo_id):
    return HttpResponse("You're looking at todo %s" % todo_id)

