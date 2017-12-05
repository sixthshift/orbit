from django.conf.urls import url
from .views import PageDetailView, PageCreateView, PageUpdateView, PageHistoryView, PageIndexView

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/update/?$',
        view=PageUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/history/?$',
        view=PageHistoryView.as_view(),
        name='history'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/?$',
        view=PageDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'',
        view=PageIndexView.as_view(),
        name='index'
    ),
]
