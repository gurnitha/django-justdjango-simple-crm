# apps/leads/models.py

# Django modules
from django.contrib import admin
from django.urls import path, include

# Locals
from apps.leads.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('leads/', include('apps.leads.urls', namespace="leads")),
]