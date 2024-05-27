from django.contrib import admin
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

    class Meta:
        model = FoodItem


admin.site.register(Category)
admin.site.register(UserFoodItem)
admin.site.register(FoodItem, FoodAdmin)
