from django.contrib import admin
from .models import User, Card, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Card)

# Register your models here.
