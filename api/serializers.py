from rest_framework import serializers
from posts.models import Post, Category, Comment
from users.models import School
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','body','date','category','author')
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post','comment','author')
    
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name')
