from .models import Card, User
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'pk',
            'user',
            'occasion',
            'frontDescription',
            'backDescription',
            'created_at',
            'image',
            'profile_pic',
            'liked',
            'has_back',
            'COLOR_CHOICES',
            'card_color',
            'BORDER_DESIGN_CHOICES',
            'border'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
        )