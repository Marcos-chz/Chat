from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nickname