# Generated by Django 4.0.4 on 2022-04-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_profilemodel'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='profilemodel',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_profile'),
        ),
    ]
