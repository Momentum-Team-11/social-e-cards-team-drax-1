from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import URLField
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        REQUIRED_FIELDS = ['username', 'password']
        return user

class User(AbstractUser):
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='User', blank=True)

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)

class Card(models.Model):
    occasion= models.CharField(max_length=50, blank=True)
    frontDescription= models.CharField(max_length=250, blank=True)
    backDescription= models.CharField(max_length=250, blank=True)
    user= models.ForeignKey(User, related_name="card", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=datetime.now)
    image = models.URLField(max_length=500, blank=True)
    profile_pic = models.URLField(max_length=500, blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_like')
    has_back = models.CharField(max_length=10, default="false")
    
    #Card Alignment
    THE_START = 'Start'
    THE_END = 'End'
    FLEX_START ='Flex-Start'
    FLEX_END = 'Flex-End'
    FLEX_CENTER = 'Center'
    FLEX_LEFT = 'Left'
    FLEX_RIGHT = 'Right'
    NORMAL = 'Normal'
    SPACE_BETWEEN = 'Space-Between'
    SPACE_AROUND = 'Space-Around'
    SPACE_EVENLY = 'Space-Evenly'
    STRETCH = 'Stretch'
    SAFE = 'Safe'
    UNSAFE = 'Unsafe'
    CARD_ALIGNMENT_CHOICES = [
        (THE_START, 'Start'), (THE_END, 'End'), (FLEX_START, 'Flex-Start'), (FLEX_END, 'Flex-End'),
        (FLEX_CENTER, 'Center'), (FLEX_LEFT, 'Left'), (FLEX_RIGHT, 'Right'), (NORMAL, 'Normal'), (SPACE_BETWEEN, 'Space-Between'),
        (SPACE_AROUND, 'Space-Around'), (SPACE_EVENLY, 'Space-Evenly'), (STRETCH, 'Stretch'), (SAFE, 'Safe'), (UNSAFE, 'Unsafe')]
    card_alignment = models.CharField(max_length=200, blank=True, choices=CARD_ALIGNMENT_CHOICES)

    #Card FONTS
    ROBOTO = 'Roboto'
    OPEN_SANS = 'Open Sans'
    LATO = 'Lato'
    OSWALD = 'Oswald'
    CONCERT_ONE = 'Concert One'
    CARD_FONT_CHOICES = [(ROBOTO,'Roboto'),(OPEN_SANS, 'Open Sans'), (LATO, 'Lato'), (OSWALD , 'Oswald'), (CONCERT_ONE, 'Concert One')]
    card_font = models.CharField(max_length=200, blank=True, choices=CARD_FONT_CHOICES)

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


