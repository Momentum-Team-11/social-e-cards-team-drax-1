# Generated by Django 4.0.3 on 2022-04-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_card_border_card_card_color_card_liked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='profile_pic',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
