"""Ecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # path('follow/<int:pk>/', api_views.FollowView.as_view({'post': 'follow'})),
    # path('unfollow/<int:pk>/', api_views.FollowView.as_view({'post': 'unfollow'})),

# api URLs
    path('api-auth/', include('rest_framework.urls')),
    path('api/user/', api_views.UserListView.as_view()),
    path('api/cards/', api_views.PublicCardListView.as_view()),
    path('api/cards/<int:pk>/', api_views.CardDetailsView.as_view()),
    path('api/user/<int:pk>/', api_views.UserDetailsView.as_view()),
    path('api/user-created-cards/', api_views.UserCreatedCardListView.as_view()),
    path('api/following/', api_views.UserFollowedCardListView.as_view()),
    path('api/following/<int:pk>/', api_views.FollowView.as_view()),
    path('api/unfollow/<int:pk>/', api_views.UnFollowView.as_view()),
    path('api/like/<int:pk>/', api_views.LikeView.as_view()),
    path('api/unlike/<int:pk>/', api_views.UnLikeView.as_view()),
    path('api/search/', api_views.CardSearchView.as_view()),
    path('api/draft/', api_views.UserCreatedDraftCardListView.as_view()),
    path('api/draft/<int:pk>/', api_views.DraftCardDetailsView.as_view()),
    path('api/profile/list/', api_views.ProfileList.as_view()),
    path('api/profile/<int:pk>/', api_views.ProfileDetail.as_view()),
    path('api/comment/list/', api_views.CommentList.as_view()),
    path('api/comment/<int:pk>/', api_views.CommentDetail.as_view()),
    path('api/specific-comment/<int:pk>/', api_views.SpecificCommentListView.as_view()),

]
