from django.contrib.auth.models import AbstractUser
from django.db import models

class OdooUser(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.username