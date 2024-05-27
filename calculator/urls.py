from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.user_page, name='UserPage'),
    path('home/', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('calorie-calculator/', views.calorie_calculator, name='CalorieCalculator'),
    path('product/', views.food_item, name='FoodItem'),
    path('create-food-item/', views.create_food_item, name='CreateFoodItem'),
    path('add-food-item/', views.add_food_item, name='AddFoodItem'),
    path('orm-calculator/', views.orm_calculator, name='ORMCalculator'),
    path('orm-calculator/orm/', views.orm, name='orm'),
    path('calorie-maintenance/', views.cm, name='cm'),
    path('calorie-maintenance/cmr/', views.cmr, name='cmr'),

]
