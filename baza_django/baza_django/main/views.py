from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from main.menudata import massiv

from main.mealrecipe import massiv_recipe

from main.massiv_poiska import massiv_poiska

def main_meals(request):
    tmp1 = {'menuData': massiv()}
    return render(request, 'main/main_meals.html', tmp1)
def about(request):
    return render(request, 'main/about.html')
def profile(request):
    return render(request, 'main/profile.html')
def filters(request):
    return render(request, 'main/filters.html')
def first_meal(request):
    tmp2 = {'mealRecipe': massiv_recipe()}
    return render(request, 'main/first_meal.html', tmp2)
def test_poiska(request):
    tmp3 = {'massivPoiska': massiv_poiska()}
    return render(request, 'main/test_poiska.html', tmp3)
