from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

app_name = 'recipes'

# Create your views here.


def home(request):
    # apenas receitas publicadas
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    return render(request, "recipes/pages/home.html", context={
        'name': 'Sergionics',
        'recipes': recipes
    })


def category(request, category_id):

    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    return render(request, "recipes/pages/category.html", context={
        'name': 'Sergionics',
        'recipes': recipes
    })


def recipe(request, id):

    recipe = Recipe.objects.get(pk=id)

    return render(request, "recipes/pages/recipe-view.html", context={
        'name': 'Sergionics',
        'recipe': recipe,
        'is_detail_page': True
    })
