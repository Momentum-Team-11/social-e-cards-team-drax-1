# Generated by Django 4.0.3 on 2022-04-10 00:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='liked',
        ),
        migrations.AddField(
            model_name='card',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
