from django.http import JsonResponse
from django.shortcuts import render
from main.connection_with_backend import massiv_main
from main.connection_with_backend import massiv_recipe
from main.connection_with_backend import massiv_poiska
from main.connection_with_backend import find_dishes_starting_with
def main_meals(request):
    tmp1 = {'menuData': massiv_main()}
    return render(request, 'main/main_meals.html', tmp1)
def about(request):
    return render(request, 'main/about.html')
def profile(request):
    return render(request, 'main/profile.html')
def filters(request):
    return render(request, 'main/filters.html')
def first_meal(request):
    tmp2 = {'mealRecipe': massiv_recipe(id)}
    return render(request, 'main/first_meal.html', tmp2)
def get_recipe(request):
    index = request.GET.get('index', None)
    if index is not None:
        recipe_data = massiv_recipe(int(index))
        return JsonResponse(recipe_data)
    else:
        return JsonResponse({'error': 'Отсутствует параметр индекса.'}, status=400)
def get_suggestions(request):
    input_text = request.GET.get('input', '')
    suggestions_list = massiv_poiska(input_text)
    return JsonResponse({'suggestions': suggestions_list})
def get_suggestions_in_containers(request):
    input_text = request.GET.get('input', '')
    suggestions_list = find_dishes_starting_with(input_text)
    return JsonResponse({'suggestions': suggestions_list})
