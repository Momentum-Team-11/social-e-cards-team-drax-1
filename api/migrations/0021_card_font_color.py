# Generated by Django 4.0.4 on 2022-04-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='font_color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Red', 'Red'), ('White', 'White'), ('Gray', 'Gray'), ('Yellow', 'Yellow'), ('Silver', 'Silver')], max_length=200),
        ),
    ]
