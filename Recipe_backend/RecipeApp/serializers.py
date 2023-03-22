from rest_framework import serializers
from .models import Category, User, Recipe, Like

class CategorySerializer(serializers.ModelSerializer):
    categoryImage = serializers.ImageField(required=False)
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer()
    
    class Meta:
        model = Recipe
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

