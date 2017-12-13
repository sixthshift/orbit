from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import PageForm
from .models import Page


class PageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pages/detail.html'
    model = Page


class PageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pages/form.html'
    model = Page
    form_class = PageForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            form = form_class(**self.get_form_kwargs())
        else:
            form = form_class()
        return form

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PageCreateView, self).get_form_kwargs()
        kwargs['creator'] = self.request.user
        return kwargs

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()


class PageHistoryView(LoginRequiredMixin, DetailView):
    template_name = 'pages/history.html'
    model = Page

    def get_context_data(self, *args, **kwargs):
        context = super(PageHistoryView, self).get_context_data(*args, **kwargs)
        context['object_list'] = Page.objects.filter(group_id=self.object.group_id).order_by('creation_date')
        return context


class PageIndexView(LoginRequiredMixin, ListView):
    template_name = 'pages/index.html'
    model = Page
    queryset = Page.active_pages.all()


class PageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pages/form.html'
    model = Page
    form_class = PageForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            form = form_class(**self.get_form_kwargs())
        else:
            form = super(PageUpdateView, self).get_form(form_class)
        return form

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PageUpdateView, self).get_form_kwargs()
        kwargs['creator'] = self.request.user
        kwargs['version'] = self.object.version
        return kwargs

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()
