from .urls import *
from debug_toolbar import urls as debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

third_party_patterns += [
    url(r'^__debug__/', include(debug_toolbar)),
]

django_patterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
django_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = local_patterns + third_party_patterns + django_patterns
