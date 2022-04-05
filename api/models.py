from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import URLField


# Create your models here.

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Card(models.Model):
    occasion= models.CharField(max_length=50, blank=True)
    frontDescription= models.CharField(max_length=250, blank=True)
    backDescription= models.CharField(max_length=250)
    user= models.ForeignKey(User, related_name="cards", on_delete=models.CASCADE, null=True, blank=True)
    created_at= models.DateField(auto_now_add=True)
    image = models.URLField(max_length=200, blank=True)
    has_back=models.BooleanField(default=False)

    def __str__(self):
        return self.occasion