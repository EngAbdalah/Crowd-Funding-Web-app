from rest_framework import serializers
from .models import Comment, Reply, Rate
from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at',)