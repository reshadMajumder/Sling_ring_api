from rest_framework import serializers
from .models import Post, Star

class PostSerializer(serializers.ModelSerializer):
    stars_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'stars_count']

    def get_stars_count(self, obj):
        return Star.objects.filter(post=obj).count()


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ['user', 'post', 'created_at']
