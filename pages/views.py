from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import PageForm
from .models import Page


class PageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pages/detail.html'
    model = Page

    def get_object(self, queryset=None):
        self.kwargs[self.slug_url_kwarg] = self.kwargs[self.slug_url_kwarg].upper()
        return super(PageDetailView, self).get_object(queryset)

    def render_to_response(self, context, **response_kwargs):
        page = Page.objects.get_subclass(pk=self.object.pk)
        if type(page) == self.model:
            return super(PageDetailView, self).render_to_response(context, **response_kwargs)
        else:
            return redirect(page, permanent=True)


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
        return reverse('pages:detail', kwargs={'slug': self.object.slug})


class PageHistoryView(LoginRequiredMixin, DetailView):
    template_name = 'pages/history.html'
    model = Page

    def get_context_data(self):
        context = super(PageHistoryView, self).get_context_data(*args, **kwargs)
        context['object_list'] = Page.objects.filter(group_id=self.object.group_id).order_by('creation_date').select_subclasses()
        return context


class PageIndexView(LoginRequiredMixin, ListView):
    template_name = 'pages/index.html'
    model = Page
    queryset = Page.objects.filter(is_removed=False).select_subclasses()  # Refers to the 'All' Tab in the index

    def get_context_data(self, *args, **kwargs):
        context = super(PageIndexView, self).get_context_data(*args, **kwargs)
        context['recently_modified'] = Page.objects.filter(is_removed=False).order_by('creation_date').select_subclasses()
        return context


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
        return reverse('pages:detail', kwargs={'slug': self.object.slug})

    def render_to_response(self, context, **response_kwargs):
        page = Page.objects.get_subclass(pk=self.object.pk)
        if type(page) == self.model and not page.is_removed:
            return super(PageUpdateView, self).render_to_response(context, **response_kwargs)
        else:
            return redirect(page, permanent=True)
