
from django.urls import path, include
from apps.post.api.v1.views import PostViewSet, PostScoreViewSet

app_name = 'post.api.v1'

urlpatterns = [
    path('', PostViewSet.as_view({'get': 'list'}),
         name='posts'),
    path('<int:post_id>/score/',
         PostScoreViewSet.as_view({'post': 'create'}), name='post_score')
]
