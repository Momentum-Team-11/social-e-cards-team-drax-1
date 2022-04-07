from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from .models import Card, User, Profile
from .serializer import CardSerializer, UserSerializer 
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView 

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly)

class CardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class FollowView(viewsets.ViewSet):
#     queryset = Profile.objects

#     def follow(self, request, pk):
#         # your follow code
#         own_profile = request.user.profile_set.first()  
#         following_profile = Profile.objects.get(id=pk)
#         own_profile.following.add(following_profile)
#         return Response({'message': 'now you are following'}, status=status.HTTP_200_OK)

#     def unfollow(self, request, pk):
#         # your unfollow code
#         own_profile = request.user.profile_set.first()  
#         following_profile = Profile.objects.get(id=pk)
#         own_profile.following.remove(following_profile)
#         return Response({'message': 'you are no longer following him'}, status=status.HTTP_200_OK)
