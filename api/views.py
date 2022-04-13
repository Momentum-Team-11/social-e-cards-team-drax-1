
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets, filters, status
from .models import Card, ProfileModel, User, Draft, Comment
from .serializer import CardSerializer, CommentSerializer, ProfileSerializer, UserSerializer, DraftCardSerializer 
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView 
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class PublicCardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('-created_at')
    serializer_class = CardSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserFollowedCardListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permissions = (IsOwnerOrReadOnly,)

    
    def get_queryset(self):
        currentUser = User.objects.get(username=self.request.user)
        return currentUser.following.all()

    # def get_queryset(self):
    #     user_id = self.request.GET.get('current_user_id', None)
    #     return User.objects.filter(following__id=user_id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreatedCardListView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    permissions = (IsOwnerOrReadOnly,)
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Card.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def follow(request, pk):
#     own_profile = request.user
#     following_profile = User.objects.get(id=pk)
#     own_profile.following.add(following_profile)  
#     return Response({'message': 'now you are following'})

class FollowView(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                
        def post(request, self, pk,format=None):    
            current_profile = self.user
            other_profile = pk
            current_profile.following.add(other_profile)

            return Response({"Requested" : "Follow request has been sent!!"},status=status.HTTP_200_OK)

class UnFollowView(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                
        def delete(request, self, pk,format=None):    
            current_profile = self.user
            other_profile = pk
            current_profile.following.remove(other_profile)

            return Response({"Requested" : "Unfollowed!"},status=status.HTTP_200_OK)

class LikeView(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                
        def post(request, self, pk,format=None):    
            current_profile = self.user
            current_card = Card.objects.get(id=pk)
            current_card.like.add(current_profile)

            return Response({"Requested" : "You have liked this card!"},status=status.HTTP_200_OK)


class UnLikeView(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                
        def delete(request, self, pk,format=None):    
            current_profile = self.user
            current_card = Card.objects.get(id=pk)
            current_card.like.remove(current_profile)

            return Response({"Requested" : "You have Unliked this card!"},status=status.HTTP_200_OK)

# Searching
class CardSearchView(generics.ListAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Card.objects.all()
        occasion = self.request.query_params.get('occasion')
        if occasion is not None:
            queryset = queryset.filter(occasion__icontains=occasion)
        return queryset


# Draft
class UserCreatedDraftCardListView(generics.ListCreateAPIView):
    serializer_class = DraftCardSerializer
    permissions = (IsOwnerOrReadOnly,)
    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Draft.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DraftCardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DraftCardSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Draft.objects.filter(filters)



class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = ProfileModel.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = ProfileModel.objects.all()


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
