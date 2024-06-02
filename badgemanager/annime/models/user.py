from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    job = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="users/")

    has_starter = models.BooleanField(default=False)
    has_pionner = models.BooleanField(default=False)
    has_collector = models.BooleanField(default=False)
