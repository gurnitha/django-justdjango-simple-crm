# apps/leads/models.py

# Django modules
from django.contrib import admin
from django.urls import path, include

# Locals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('apps.leads.urls', namespace="leads")),
]