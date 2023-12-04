from rest_framework import serializers
from .models import Forum, Post


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('title', 'description', 'user')
