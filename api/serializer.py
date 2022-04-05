from .models import Card, User
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'pk',
            'user',
            'occasion',
            'frontdescription',
            'backdescription',
            'created_at',
            'image',
            'has_back',
        )

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
        )