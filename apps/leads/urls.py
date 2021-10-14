# apps/leads/urls.py

# Django modules
from django.urls import path

# Locals
from apps.leads.views import lead_list, lead_detail

app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<pk>/', lead_detail),
]


    