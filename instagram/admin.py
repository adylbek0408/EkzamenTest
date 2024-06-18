from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Story)
admin.site.register(Follow)
admin.site.register(Group)
