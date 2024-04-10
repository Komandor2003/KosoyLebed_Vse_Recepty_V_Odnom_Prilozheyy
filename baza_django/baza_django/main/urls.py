from django.urls import path
from . import views
from .views import get_recipe
urlpatterns = [
    path('', views.main_meals),
    path('about', views.about),
    path('main', views.main_meals),
    path('profile', views.profile),
    path('filters', views.filters),
    path('first_meal', views.first_meal),
    path('get_recipe/', get_recipe, name='get_recipe'),
    path('get_suggestions/', views.get_suggestions, name='get_suggestions'),
    path('get_suggestions_in_containers/', views.get_suggestions_in_containers, name='get_suggestions_in_containers'),
]