from rest_framework import generics, serializers
from post.models import User, Post, Comment
from demoProject.common.extra_serializer import get_extra_fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.SerializerMethodField('get_last_comment')
    total_comment = serializers.SerializerMethodField('get_total_comment')

    @staticmethod
    def get_last_comment(post):
        last_comment = Comment.objects.filter(post_id=post.id).order_by('created_at').first()
        return last_comment.content if last_comment else ""

    @staticmethod
    def get_total_comment(post):
        total_comment = Comment.objects.filter(post_id=post.id).count()
        return total_comment

    class Meta:
        model = Post
        extra_fields = ['total_comment', 'comment']
        fields = get_extra_fields(Post, extra_fields)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.nickname
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
