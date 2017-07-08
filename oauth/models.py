from django.db import models
from django.utils import timezone



class User(models.Model):
    name = models.CharField(max_length=512)
    oauth_type = models.CharField(max_length=128)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_visit_date = models.DateTimeField(auto_now=True)
