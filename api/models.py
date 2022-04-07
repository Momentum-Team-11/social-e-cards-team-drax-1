from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import URLField
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)

class Card(models.Model):
    occasion= models.CharField(max_length=50, blank=True)
    frontDescription= models.CharField(max_length=250, blank=True)
    backDescription= models.CharField(max_length=250)
    user= models.ForeignKey(User, related_name="cards", on_delete=models.CASCADE, null=True, blank=True)
    created_at= models.DateField(auto_now_add=True)
    image = models.URLField(max_length=500, blank=True)
    profile_pic = models.URLField(max_length=500, blank=True)
    liked = models.CharField(max_length=10, default=False)
    has_back = models.CharField(max_length=10, default=False)
    
    # CARD COLORS AND BORDER DESIGN
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    VIOLET = 'Violet'
    BEADED = 'Beaded'
    CHAIN_LINK = 'Chain Link'
    SUBTLE_TRIPLE = 'Subtle Triple'
    COLOR_CHOICES = [(RED,'Red'), (BLUE,'Blue'), (GREEN,'Green'), (YELLOW, 'Yellow'), (VIOLET,'Violet')]
    card_color = models.CharField(max_length=200, blank=True, choices=COLOR_CHOICES)
    BORDER_DESIGN_CHOICES = [(BEADED,'Beaded'),(CHAIN_LINK,'Chain Link'),(SUBTLE_TRIPLE,'Subtle Triple')]
    border = models.CharField(max_length=200, blank=True, choices=BORDER_DESIGN_CHOICES)



    def __str__(self):
        return self.occasion