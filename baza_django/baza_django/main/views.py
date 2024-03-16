from django.shortcuts import render
# Create your views here.
from main.mytest import meal, recipe

tmp = {"meal": meal(), "recipe": recipe()}
print(tmp)


def main_meals(request):
    return render(request, 'main/main_meals.html', tmp)


def about(request):
    return render(request, 'main/about.html')


def profile(request):
    return render(request, 'main/profile.html')


def filters(request):
    return render(request, 'main/filters.html')


def first_meal(request):
    return render(request, 'main/first_meal.html')
