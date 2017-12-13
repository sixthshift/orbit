from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.manager import Manager
from django.urls import reverse
from model_utils.managers import SoftDeletableManager
from model_utils.models import SoftDeletableModel
import uuid
from accounts.models import Account


class BasePage(SoftDeletableModel):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True)
    creator = models.ForeignKey(Account)
    creation_date = models.DateTimeField(auto_now_add=True)
    group_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    version = models.IntegerField()
    changelog = models.CharField(max_length=50, blank=True)

    objects = Manager()
    active_pages = SoftDeletableManager()

    class Meta:
        abstract = True

    @property
    def category(self):
        return self.__class__.__name__


class Page(BasePage):

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'pk': self.pk})

    def get_absolute_history_url(self):
        return reverse('pages:history', kwargs={'pk': self.pk})
