# Generated by Django 4.0.3 on 2022-04-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_card_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
