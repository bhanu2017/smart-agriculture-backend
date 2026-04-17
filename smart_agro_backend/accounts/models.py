from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.username
