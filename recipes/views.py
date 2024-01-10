from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import Http404

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

    # recipes = Recipe.objects.filter(
    #    category__id=category_id,
    #    is_published=True
    # ).order_by('-id')

    # if not recipes:
    #    raise Http404('Não encontrado...')

    recipes = get_list_or_404( Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(request, "recipes/pages/category.html", context={
        'name': 'Sergionics',
        'recipes': recipes,
        'title': f'{recipes[0].category.name} -  Category | '
    })


def recipe(request, id):

    recipe = Recipe.objects.get(pk=id)

    return render(request, "recipes/pages/recipe-view.html", context={
        'name': 'Sergionics',
        'recipe': recipe,
        'is_detail_page': True
    })
