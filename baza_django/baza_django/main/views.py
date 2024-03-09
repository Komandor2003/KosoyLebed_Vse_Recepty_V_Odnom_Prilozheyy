from django.shortcuts import render
# Create your views here.
def main_meals(request):
    return render(request, 'main/main_meals.html')
def about(request):
    return render(request, 'main/about.html')
