from django.urls import path
from .views import (UserProfileView, FollowView, PostView, PostLikeView, CommentView, CommentLikeView, StoryView,
                    GroupView)

urlpatterns = [
    path('user_profile/', UserProfileView.as_view({'get': 'list', 'post': 'create'}), name='user_profile_list'),
    path('user_profile/<int:pk>/', UserProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),

    path('follow/', FollowView.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('follow/<int:pk>/', FollowView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow_detail'),

    path('post/', PostView.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
    path('post/<int:pk>/', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='post_detail'),

    path('post_like/', PostLikeView.as_view({'get': 'list', 'post': 'create'}), name='post_like_list'),
    path('post_like/<int:pk>/', PostLikeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='post_like_detail'),

    path('comment/', CommentView.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),

    path('comment_like/', CommentLikeView.as_view({'get': 'list', 'post': 'create'}), name='comment_like_list'),
    path('comment_like/<int:pk>/', CommentLikeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_like_detail'),

    path('story/', StoryView.as_view({'get': 'list', 'post': 'create'}), name='story_list'),
    path('story/<int:pk>/', StoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='story_detail'),

    path('group/', GroupView.as_view({'get': 'list', 'post': 'create'}), name='group_list'),
    path('group/<int:pk>/', GroupView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='group_detail'),
]
