from django.conf.urls import url
from .views import (
    EventCalendarView,
    EventCreateView,
    EventDetailView,
    EventUpdateView,
    EventHistoryView,
    EventIndexView
)

urlpatterns = [
    url(
        regex=r'^calendar/?$',
        view=EventCalendarView.as_view(),
        name='calendar'
    ),
    url(
        regex=r'^create/?$',
        view=EventCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/update/?$',
        view=EventUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/history/?$',
        view=EventHistoryView.as_view(),
        name='history'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/?$',
        view=EventDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'',
        view=EventIndexView.as_view(),
        name='index'
    ),
]
