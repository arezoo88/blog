from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.post.models import Post, PostScore
from apps.post.api.v1.serializers import PostSerializer, PostScoreSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostScoreViewSet(ModelViewSet):
    queryset = PostScore
    serializer_class = PostScoreSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
