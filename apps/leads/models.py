# apps/leads/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(models.Model):
    customuser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

