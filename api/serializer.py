from socketserver import ThreadingUDPServer
from .models import Card, User, Draft
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_pk= serializers.PrimaryKeyRelatedField(read_only='True', source="user")
    created_at=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Card
        fields = (
            'pk',
            'user_pk',
            'username',
            'occasion',
            'frontDescription',
            'backDescription',
            'created_at',
            'image',
            'profile_pic',
            'like',
            'has_back',
            'card_color',
            'border'
        )

class DraftCardSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_pk= serializers.PrimaryKeyRelatedField(read_only='True', source="user")
    created_at=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Draft
        fields = (
            'pk',
            'user_pk',
            'username',
            'occasion',
            'frontDescription',
            'backDescription',
            'created_at',
            'image',
            'profile_pic',
            'like',
            'has_back',
            'card_color',
            'border'
        )


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    card = CardSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'following',
            'card'
        )
        def create(self, validated_data):
            cards = validated_data.pop('cards')
            user_instance = User.objects.create(**validated_data)
            for card in cards:
                User.objects.create(user=user_instance, **card)
            return user_instance