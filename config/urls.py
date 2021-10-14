# apps/leads/models.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Locals
from apps.leads.views import (
    # landing_page, 
    LandingPageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('apps.leads.urls', namespace="leads")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)