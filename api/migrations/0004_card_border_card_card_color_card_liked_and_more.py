# Generated by Django 4.0.3 on 2022-04-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_card_occasion'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='border',
            field=models.CharField(blank=True, choices=[('Beaded', 'Beaded'), ('Chain Link', 'Chain Link'), ('Subtle Triple', 'Subtle Triple')], max_length=200),
        ),
        migrations.AddField(
            model_name='card',
            name='card_color',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Violet', 'Violet')], max_length=200),
        ),
        migrations.AddField(
            model_name='card',
            name='liked',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='card',
            name='profile_pic',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='has_back',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
