# users/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username