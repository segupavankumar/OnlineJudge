from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    score = models.FloatField(default=0)
    solved = models.IntegerField(default=0)

    def __str__(self):
        return self.username