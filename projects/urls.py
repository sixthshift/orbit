from django.conf.urls import url
from .views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectIndexView,
    ProjectUpdateView,
    TaskCreateView,
    TaskDetailView,
    TaskIndexView,
)

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=ProjectCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/task/?$',
        view=TaskIndexView.as_view(),
        name='task_index'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/task/create/?$',
        view=TaskCreateView.as_view(),
        name='task_create'
    ),
    url(
        regex=r'^(?P<project_pk>[^/]+)/task/(?P<task_pk>[^/]+)/?$',
        view=TaskDetailView.as_view(),
        name='task_detail'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/update/?$',
        view=ProjectUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/?$',
        view=ProjectDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'',
        view=ProjectIndexView.as_view(),
        name='index'
    ),
]
