from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Project
from .models import Todo


class IndexView(generic.ListView):
    template_name = 'todo_app/index.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'todo_app/project.html'


class TodoView(generic.DetailView):
    model = Todo
    template_name = 'todo_app/todo.html'


def create_todo(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    try:
        text = request.POST['text']
        priority = request.POST['priority']
    except (KeyError, Project.DoesNotExist):
        return render(request, 'todo_app/project.html', {
            'project': project,
            'error_message': 'text is missing'
        })
    else:
        todo = project.todo_set.create(text=text, priority=priority, done=False)
        todo.save()
    return HttpResponseRedirect(reverse('todo_app:todo', args=(todo.id,)))
