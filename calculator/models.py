from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    fat = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    protein = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    calories = models.DecimalField(max_digits=6, decimal_places=1, default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class UserFoodItem(models.Model):
    users = models.ManyToManyField(User, blank=True)
    food_item = models.ManyToManyField(FoodItem)
