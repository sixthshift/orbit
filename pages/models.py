# from ckeditor.fields import RichTextField
from markdownx.models import MarkdownxField
from django.db import models
from django.urls import reverse
from markdownx.utils import markdownify
from model_utils.managers import InheritanceManager
from uuslug import uuslug
from accounts.models import Account


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = MarkdownxField(blank=True)
    author = models.ForeignKey(Account)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True)
    version = models.IntegerField()
    active = models.BooleanField(default=True)

    # Downcast all pages to subclasses if applicable
    objects = InheritanceManager()

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'slug': self.slug})

    @property
    def markdown(self):
        return markdownify(self.content)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Page, self).save(*args, **kwargs)
