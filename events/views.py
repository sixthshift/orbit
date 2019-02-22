from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from .forms import EventForm
from .models import Event
from pages.views import PageCreateView, PageDetailView, PageHistoryView, PageUpdateView


class EventCalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'events/calendar.html'
    model = Event

    def get_context_data(self, *args, **kwargs):
        context = super(EventCalendarView, self).get_context_data(*args, **kwargs)
        return context


class EventCreateView(PageCreateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm


class EventDetailView(PageDetailView):
    template_name = 'events/detail.html'
    model = Event

    def render_to_response(self, context, **response_kwargs):
        response = super(EventDetailView, self).render_to_response(context, **response_kwargs)
        return response

    def as_view(self, cls, **initkwargs):
        view = super(EventDetailView, self).as_view(cls, **initkwargs)
        return view


class EventHistoryView(PageHistoryView):
    model = Event


class EventIndexView(LoginRequiredMixin, ListView):
    template_name = 'events/index.html'
    model = Event
    queryset = Event.objects.filter(is_removed=False)
    ordering = ['-creation_date']


class EventUpdateView(PageUpdateView):
    template_name = 'events/form.html'
    model = Event
    form_class = EventForm
