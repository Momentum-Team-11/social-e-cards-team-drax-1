from django.contrib import admin
from .models import User, Card, ProfileModel, Comment

admin.site.register(User)
admin.site.register(ProfileModel)
admin.site.register(Card)
admin.site.register(Comment)
# Register your models here.
