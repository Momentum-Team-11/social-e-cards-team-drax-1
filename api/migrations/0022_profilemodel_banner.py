# Generated by Django 4.0.3 on 2022-04-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_card_font_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='banner',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]