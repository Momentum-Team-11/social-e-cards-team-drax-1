from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Card, User
from .serializer import CardSerializer, UserSerializer 
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView 

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly)

