from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe")
]
