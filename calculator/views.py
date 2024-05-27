from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .filters import FoodItemFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@staff_member_required
def home(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:]
    users = User.objects.all()
    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               'users': users,
               }
    return render(request, 'main.html', context)


def about(request):
    return render(request, "about.html")



def food_item(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt = snacks.count()
    context = {'breakfast': breakfast,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'food_item.html', context)


def user_page(request):
    return render(request, 'user_page.html')


def calorie_calculator(request):
    user = request.user
    food_items = FoodItem.objects.filter()
    my_filter = FoodItemFilter(request.GET, queryset=food_items)
    food_items = my_filter.qs
    total = UserFoodItem.objects.all()
    my_food_items = total.filter(users=user)
    cnt = my_food_items.count()
    queryset_food = []
    final_food_items = []
    total_calories = 0
    for food in my_food_items:
        queryset_food.append(food.fooditem.all())
    for items in queryset_food:
        for food_items in items:
            final_food_items.append(food_items)
    for foods in final_food_items:
        total_calories += foods.calorie
    calories_left = 2000 - total_calories
    context = {'calories_left': calories_left,
               'total_calories': total_calories,
               'cnt': cnt,
               'final_food_items': final_food_items,
               'food_items': food_items,
               'my_filter': my_filter,
               }
    return render(request, 'calorie_calculator.html', context)


def orm_calculator(request):
    context = {'form': ORMForm}
    return render(request, 'orp_max.html', context)


def orm(request):
    w = float(request.GET['weight'])
    r = int(request.GET['reps'])
    u = str(request.GET['units'])
    if units == 'lb':
        w = w/2.205
    rml = w * (r ** 0.10)
    rmb = w/(1.0278 - (0.0278 * r))
    rmo = w*(1 + (r / 40))
    if r == 0:
        rm = 0
        return render(request, "orp_max_result.html", {"rm": rm})
    if r == 1:
        rm = w
    else:
        if r < 6:
            rm = int(rmb)
        elif r < 11:
            rm = int(rmo)
        else:
            rm = int(rml)
    rm2 = int(0.943*rm)
    rm3 = int(0.906*rm)
    rm4 = int(0.881*rm)
    rm5 = int(0.856*rm)
    rm6 = int(0.831*rm)
    rm7 = int(0.807*rm)
    rm8 = int(0.786*rm)
    rm9 = int(0.765*rm)
    rm10 = int(0.744*rm)
    rm11 = int(0.723*rm)
    rm12 = int(0.703*rm)
    rm13 = int(0.688*rm)
    rm14 = int(0.675*rm)
    rm15 = int(0.662*rm)
    rm16 = int(0.65*rm)
    rm17 = int(0.638*rm)
    rm18 = int(0.627*rm)
    rm19 = int(0.616*rm)
    rm20 = int(0.606*rm)
    context =  {"rm": rm,
                "rm2": rm2,
                "rm3": rm3,
                "rm4": rm4,
                "rm5": rm5,
                "rm6": rm6,
                "rm7": rm7,
                "rm8": rm8,
                "rm9": rm9,
                "rm10": rm10,
                "rm11": rm11,
                "rm12": rm12,
                "rm13": rm13,
                "rm14": rm14,
                "rm15": rm15,
                "rm16": rm16,
                "rm17": rm17,
                "rm18": rm18,
                "rm19": rm19,
                "rm20": rm20,
                "units": u,
                }
    return render(request, "orp_max_result.html", context)


def cm(request):
    context = {'form': CMForm}
    return render(request, 'calorie_maintenance.html', context)


def cmr(request):
    a = float(request.GET['age'])
    ecm = 0
    floatt = lambda x: float(x.strip() or 0)
    bf = floatt(request.GET.get('bf', 0))
    s = str(request.GET['sex'])
    g = 0
    if s == 'female':
        g = 1
    u = str(request.GET['units'])
    w = float(request.GET['weight'])
    h = float(request.GET['height'])
    if u == 'imperial':
        w = w/2.205
        h = h*2.54
    act = str(request.GET['activeness'])
    p = str(request.GET.get('pregnant', 0))
    lac = str(request.GET.get('lactating', 0))
    dci = 0

    bmi = round(w/(h/100)**2, 1)
    bf1 = round(-44.988+(0.503*a)+(10.689*g)+(3.172*bmi)-(0.026*bmi**2)+(0.181*bmi*g)-(0.02*bmi*a)-(0.005*bmi**2*g)+(0.00021*bmi**2*a), 1)
    bbfc = 0
    if bf is False:
        bbfc = bf1
    else:
        bbfc = bf
    tbf = w*(bf/100)
    tbf1 = w*(bf1/100)
    if bf is True:
        tbfc = tbf
    else:
        tbfc = tbf1

    bmic = 0
    bfc = 0
    bfcf = 0
    tbfm1 = w*(5.9/100)
    tbfm2 = w*(10/100)
    tbfm3 = w*(16/100)
    tbfm4 = w*(21.5/100)
    tbfm5 = w*(25/100)
    tbff1 = w*(13.9/100)
    tbff2 = w*(17/100)
    tbff3 = w*(23/100)
    tbff4 = w*(28.5/100)
    tbff5 = w*(32/100)
    ffm = w-tbfc
    if bf == 0:
        bmrm = 10 * w + 6.25 * h - 5 * a + 5
        bmrf = 10 * w + 6.25 * h - 5 * a - 161
    else:
        bmrm = 370 + (21.6 * ffm)
        bmrf = 370 + (21.6 * ffm)
    ffmm1 = w-tbfm1
    ffmm2 = w-tbfm2
    ffmm3 = w-tbfm3
    ffmm4 = w-tbfm4
    ffmm5 = w-tbfm5
    ffmf1 = w-tbff1
    ffmf2 = w-tbff2
    ffmf3 = w-tbff3
    ffmf4 = w-tbff4
    ffmf5 = w-tbff5
    ffmi = ffm/(h/100)**2
    nffmi = ffmi+6.1*(1.8-(h/100))
    if bmi < 18.5:
        bmic = 'underweight'
    elif 18.5 <= bmi < 25:
        bmic = 'normal'
    elif 25 <= bmi < 30:
        bmic = 'overweight'
    elif 30 <= bmi < 35:
        bmic = 'obese'
    elif 35 <= bmi < 40:
        bmic = 'obese1'
    elif 40 <= bmi:
        bmic = 'obese2'
    if bf == 0:
        if s == 'male':
            if bf1 < 6:
                bfc = 'ef'
            elif 6 <= bf1 < 14:
                bfc = 'a'
            elif 14 <= bf1 < 18:
                bfc = 'f'
            elif 18 <= bf1 < 25:
                bfc = 'aa'
            elif 25 <= bf1:
                bfc = 'o'
        if s == 'female':
            if bf1 < 14:
                bfcf = 'ef'
            elif 14 <= bf1 < 21:
                bfcf = 'a'
            elif 21 <= bf1 < 25:
                bfcf = 'f'
            elif 25 <= bf1 < 32:
                bfcf = 'aa'
            elif 32 <= bf1:
                bfcf = 'o'
    else:
        if s == 'male':
            if bf < 6:
                bfc = 'ef'
                tbff1 = w*(5.9/100)
            elif 6 <= bf < 14:
                bfc = 'a'
                tbff2 = w*(10/100)
            elif 14 <= bf < 18:
                bfc = 'f'
                tbff3 = w*(16/100)
            elif 18 <= bf < 25:
                bfc = 'aa'
                tbff4 = w*(21.5/100)
            elif 25 <= bf:
                bfc = 'o'
                tbff5 = w*(25/100)
        if s == 'female':
            if bf < 14:
                bfcf = 'ef'
                tbff1 = w*(13.9/100)
            elif 14 <= bf < 21:
                bfcf = 'a'
                tbff2 = w*(17/100)
            elif 21 <= bf < 25:
                bfcf = 'f'
                tbff3 = w*(23/100)
            elif 25 <= bf < 32:
                bfcf = 'aa'
                tbff4 = w*(28.5/100)
            elif 32 <= bf:
                bfcf = 'o'
                tbff5 = w*(32/100)
    if p == 'on':
        dci = 300
    if lac == 'on':
        dci = dci+500
    if s == 'male':
        bmr = dci+bmrm
        dcis = bmrm*1.2
        dcil = bmrm*1.375
        dcim = bmrm*1.55
        dciv = bmrm*1.725
        dcie = bmrm*1.9
    else:
        bmr = dci+bmrf
        dcis = dci+bmrf*1.2
        dcil = dci+bmrf*1.375
        dcim = dci+bmrf*1.55
        dciv = dci+bmrf*1.725
        dcie = dci+bmrf*1.9
    if act == 'sedentary':
        ecm = dcis
    elif act == 'lightly active':
        ecm = dcil
    elif act == 'moderately active':
        ecm = dcim
    elif act == 'very active':
        ecm = dciv
    elif act == 'extremely active':
        ecm = dcie

    context = {'dci': round(int(dci)),
               'p': p,
               'lac': lac,
               'sex': s,
               'bmr': round(bmr),
               'dcis': round(dcis),
               'dcil': round(dcil),
               'dcim': round(dcim),
               'dciv': round(dciv),
               'dcie': round(dcie),
               'act': act,
               'bmi': bmi,
               'bf': bf,
               'ffm': round(ffm, 1),
               'bf1': bf1,
               'ffmi': round(ffmi, 1),
               'nffmi': round(nffmi, 1),
               'ecm': round(ecm),
               'bmic': bmic,
               'bfc': bfc,
               'tbfc': round(tbfc, 1),
               'bfcf': round(bfcf, 1),
               'tbff1': round(tbff1, 1),
               'tbff2': round(tbff2, 1),
               'tbff3': round(tbff3, 1),
               'tbff4': round(tbff4, 1),
               'tbff5': round(tbff5, 1),
               'tbfm1': round(tbfm1, 1),
               'tbfm2': round(tbfm2, 1),
               'tbfm3': round(tbfm3, 1),
               'tbfm4': round(tbfm4, 1),
               'tbfm5': round(tbfm5, 1),
               'ffmm1': round(ffmm1, 1),
               'ffmm2': round(ffmm2, 1),
               'ffmm3': round(ffmm3, 1),
               'ffmm4': round(ffmm4, 1),
               'ffmm5': round(ffmm5, 1),
               'ffmf1': round(ffmf1, 1),
               'ffmf2': round(ffmf2, 1),
               'ffmf3': round(ffmf3, 1),
               'ffmf4': round(ffmf4, 1),
               'ffmf5': round(ffmf5, 1),
               }
    return render(request, "calorie_maintenance_result.html", context)


@staff_member_required
def create_food_item(request):
    pass


def add_food_item(request):
    pass
