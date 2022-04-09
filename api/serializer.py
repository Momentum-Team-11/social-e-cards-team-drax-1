from .models import Card, User
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    class Meta:
        model = Card
        fields = (
            'pk',
            'username',
            'occasion',
            'frontDescription',
            'backDescription',
            'created_at',
            'image',
            'profile_pic',
            'liked',
            'has_back',
            'card_color',
            'border'
        )

class UserSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'following'
        )