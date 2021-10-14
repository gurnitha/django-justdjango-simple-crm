# apps/leads/models.py

# Django modules
from django.contrib import admin

# Locals
from apps.leads.models import CustomUser, Lead, Agent 

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Lead)
admin.site.register(Agent)