# apps/leads/urls.py

# Django modules
from django.urls import path

# Locals
from apps.leads.views import home_page

app_name = "leads"

urlpatterns = [
    path('all/', home_page)
]