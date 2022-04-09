from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets, filters
from .models import Card, User 
from .serializer import CardSerializer, UserSerializer 
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView 
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('-created_at')
    serializer_class = CardSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserFollowedCardListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = (filters.SearchFilter)
    search_fields = ['username']
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return User.following.filter(filters)

    # def get_queryset(self):
    #     user_id = self.request.GET.get('current_user_id', None)
    #     return User.objects.filter(following__id=user_id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreatedCardListView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly)
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Card.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


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
