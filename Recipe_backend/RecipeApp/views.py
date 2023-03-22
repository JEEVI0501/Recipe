from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, User, Recipe, Like
from .serializers import CategorySerializer, UserSerializer, RecipeSerializer, LikeSerializer

@csrf_exempt
def category_list(request):
    """
    API endpoint to get all categories
    """
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            print(serializer.errors)  # add this line to print errors to console
            return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def recipe_list(request):
    """
    API endpoint to get all recipes or add a new recipe
    """
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def recipe_detail(request, pk):
    """
    API endpoint to get a specific recipe by id
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)

@csrf_exempt
def user_recipes(request, user_id):
    """
    API endpoint to get all recipes posted by a specific user
    """
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        recipes = Recipe.objects.filter(user=user)
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def like_recipe(request, recipe_id):
    """
    API endpoint to like a recipe
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.likes += 1
        recipe.save()
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)

@csrf_exempt
def user_favourites(request, user_id):
    """
    API endpoint to get all recipes liked by a specific user
    """
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        likes = Like.objects.filter(user=user)
        serializer = LikeSerializer(likes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_detail(request, user_id):
    """
    API endpoint to get details of a specific user by id
    """
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
