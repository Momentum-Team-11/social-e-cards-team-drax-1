from .models import Card, User
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all())
    class Meta:
        model = Card
        fields = (
            'pk',
            'user',
            'owner',
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
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'following'
        )