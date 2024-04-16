from django.contrib import admin
from apps.post.models import Post, PostScore


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content',
                    'get_avg_score', 'get_number_user_score']


@admin.register(PostScore)
class PostScoreAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'get_post', 'score']

    def get_user(self, obj):
        return obj.user.username

    def get_post(self, obj):
        return obj.post.title
