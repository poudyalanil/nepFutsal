from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
