from django.core.validators import MaxValueValidator
from django.forms import ModelForm
from django import forms
from .models import *


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class UserFoodItemForm(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = '__all__'


weight_units = (
    ("kg", "kg"),
    ("lb", "lb"),
)

units = (
    ("metric", "metric (kg, cm)"),
    ("imperial", "imperial (lb, in)"),
)

sex = (
    ("male", "male"),
    ("female", "female"),
)

activity_level = (
    ('sedentary', 'sedentary (little to no exercise)'),
    ('lightly active', 'lightly active (exercise 1–3 days per week)'),
    ('moderately active', 'moderately active (exercise 3–5 days per week)'),
    ('very active', 'very active (exercise 6–7 days per week)'),
    ('extremely active', 'extremely active (exercise twice per day)'),
)


class ORMForm(forms.Form):
    weight = forms.DecimalField(max_digits=6, decimal_places=1, max_value=1500)
    reps = forms.DecimalField(max_digits=6, decimal_places=0, max_value=500)
    units = forms.ChoiceField(choices=weight_units)


class CMForm(forms.Form):
    age = forms.DecimalField(max_digits=2, decimal_places=0, min_value=15, max_value=80)
    sex = forms.ChoiceField(choices=sex)
    pregnant = forms.BooleanField(initial=False, required=False)
    lactating = forms.BooleanField(initial=False, required=False)
    units = forms.ChoiceField(choices=units)
    weight = forms.DecimalField(max_digits=4, decimal_places=1, max_value=635)
    height = forms.DecimalField(max_digits=4, decimal_places=1, max_value=272)
    activeness = forms.ChoiceField(choices=activity_level)
    bf = forms.DecimalField(label='Body Fat (not required)', help_text='%', required=False, decimal_places=1, min_value=1, max_value=80)
