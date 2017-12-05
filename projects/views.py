from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from pages.views import PageCreateView, PageDetailView, PageUpdateView
from .forms import ProjectForm, TaskForm
from .models import Project, Task


class ProjectCreateView(PageCreateView):
    template_name = 'projects/form.html'
    model = Project
    form_class = ProjectForm


class ProjectDetailView(PageDetailView):
    template_name = 'projects/detail.html'
    model = Project


class ProjectIndexView(LoginRequiredMixin, ListView):
    template_name = 'projects/index.html'
    model = Project
    queryset = Project.objects.filter(is_removed=False)


class ProjectUpdateView(PageUpdateView):
    template_name = 'projects/form.html'
    model = Project
    form_class = ProjectForm


class TaskCreateView(PageCreateView):
    template_name = 'projects/tasks/form.html'
    model = Task
    form_class = TaskForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            form = form_class(**self.get_form_kwargs())
        else:
            form = form_class()
        return form

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return kwargs

    def get_success_url(self, **kwargs):
        project_pk = self.kwargs.get('pk')
        return reverse('projects:task_detail', kwargs={'project_pk': project_pk, 'task_pk': self.object.pk})


class TaskDetailView(PageDetailView):
    template_name = 'projects/tasks/detail.html'
    model = Task

    def get_object(self):
        project_pk = self.kwargs.get('project_pk')
        project = get_object_or_404(Project, pk=project_pk)
        task_pk = self.kwargs.get('task_pk')
        return get_object_or_404(Task, task_project=project, pk=task_pk)


class TaskIndexView(PageDetailView):
    template_name = 'projects/tasks/index.html'
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(TaskIndexView, self).get_context_data(*args, **kwargs)
        context['to_do'] = Task.objects.filter(task_project=self.object, column=Project.to_do)
        context['in_progress'] = Task.objects.filter(task_project=self.object, column=Project.in_progress)
        context['completed'] = Task.objects.filter(task_project=self.object, column=Project.completed)
        return context
