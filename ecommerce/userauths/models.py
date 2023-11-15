from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email= models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100, default='0')
    
    USERNAME_FIELD = "email"      #to login with email intead of username
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username