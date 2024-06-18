from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_users')
    bio = models.TextField()
    image = models.ImageField()
    website = models.URLField()
    followers = models.IntegerField()


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users_following')
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField()
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    hashtag = models.CharField(max_length=255, null=True, blank=True)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users_post_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_comment_like')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users_story')
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateField()


class Group(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_group')
    members = models.ManyToManyField(UserProfile)
    join_key = models.CharField(max_length=120)
