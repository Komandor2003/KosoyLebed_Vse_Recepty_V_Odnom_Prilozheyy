from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_meals),
    path('about', views.about),
    path('main', views.main_meals),
    path('profile', views.profile),
    path('filters', views.filters)
]