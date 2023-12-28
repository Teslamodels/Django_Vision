from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    age = models.PositiveIntegerField(null=True, blank=True)
    