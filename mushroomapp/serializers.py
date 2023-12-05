from rest_framework import serializers
from .models import Forum, Post

# add stuff here so that the data can be accesses viewed in API

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
