from django.db import models
from django.urls import reverse
from pages.models import Page


class Project(Page):
    code = models.CharField(max_length=5)
    deadline = models.DateTimeField(blank=True, null=True)

    to_do = 0
    in_progress = 1
    completed = 2
    columns = (
        (to_do, 'to_do'),
        (in_progress, 'in_progress'),
        (completed, 'completed'),
    )

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})

    def get_absolute_task_index_url(self):
        return reverse('projects:task_index', kwargs={'pk': self.pk})


class Task(Page):
    task_project = models.ForeignKey(Project)
    column = models.CharField(max_length=1, choices=Project.columns, default=0)

    def get_absolute_url(self):
        project_pk = self.task_project.pk
        task_pk = self.pk
        return reverse('projects:task_detail', kwargs={'project_pk': project_pk, 'task_pk': task_pk})
