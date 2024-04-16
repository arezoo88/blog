from rest_framework.serializers import ModelSerializer
from apps.post.models import Post, PostScore


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'get_number_user_score', 'get_avg_score')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(self.context['request'].user)
        data['your_score'] = None
        if self.context['request'].user:
            try:
                data['your_score'] = instance.post.first().score
            except:
                pass
        return data


class PostScoreSerializer(ModelSerializer):
    class Meta:
        model = PostScore
        fields = ('user', 'post', 'score')
        read_only_fields = ['user', 'post']

    def create(self, validated_data):
        postscore, created = PostScore.objects.update_or_create(
            post=self.context['view'].kwargs.get('post_id'), user=self.context['request'].user,
            defaults={'score': validated_data.get('score', None)},

        )
        return postscore
