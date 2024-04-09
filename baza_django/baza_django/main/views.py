from django.http import JsonResponse
from django.shortcuts import render
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
    tmp2 = {'mealRecipe': massiv_recipe(id)}
    return render(request, 'main/first_meal.html', tmp2)

def test_poiska(request):
    # tmp3 = {'massivPoiska': massiv_poiska()}
    return render(request, 'main/test_poiska.html')

def get_recipe(request):
    index = request.GET.get('index', None)
    if index is not None:
        recipe_data = massiv_recipe(int(index))
        return JsonResponse(recipe_data)
    else:
        return JsonResponse({'error': 'Отсутствует параметр индекса.'}, status=400)

def get_suggestions(request):
    input_text = request.GET.get('input', '')  # Получаем ввод пользователя из GET-параметра input
    suggestions_list = massiv_poiska(input_text)  # Получаем подсказки на основе ввода пользователя
    return JsonResponse({'suggestions': suggestions_list})
