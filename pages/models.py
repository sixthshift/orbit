from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from model_utils.models import SoftDeletableModel
import uuid
from accounts.models import Account
from .managers import PageManager


class Page(SoftDeletableModel):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True)
    creator = models.ForeignKey(Account)
    creation_date = models.DateTimeField(auto_now_add=True)
    group_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    version = models.IntegerField()
    changelog = models.CharField(max_length=50, blank=True)

    objects = PageManager()

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'pk': self.pk})

    def get_absolute_history_url(self):
        return reverse('pages:history', kwargs={'pk': self.pk})

    @property
    def category(self):
        return self.__class__.__name__
