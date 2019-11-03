from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from xmtb_app.models import *
from xmtb_app.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import  Q
from django.contrib.auth.decorators import login_required

def baseindexview(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("base")
    context['login_form'] = LoginForm()
    return render(request, "login.html", context)


def login_view(request):
    context = {}
    if request.method == "POST":
        context['login_form'] = LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("base")
            else:
                context["message"] = "имя пользователя или пароль неверен!"
                return render(request, "login.html", context)
        else:
            context["login_form"] = form
            return render(request, "login.html", context)
    else:
        return redirect("home")

@login_required(login_url="/login")
def homepage(request):
    context = {}
    context['brands'] = Brands.objects.all()
    context['cities'] = Cities.objects.all()
    context['categories'] = Categories.objects.all()
    context['products'] = Products.objects.all()

    '''After code is filtering user queryset'''

    if request.GET.get('dropdown_category') or request.GET.get('dropdown_brand') or request.GET.get('dropdown_city'):
        dropdown_category = request.GET.get('dropdown_category')
        dropdown_brand = request.GET.get('dropdown_brand')
        dropdown_city = request.GET.get('dropdown_city')
        context['queryset'] = Products.objects.filter(Q(category__category=dropdown_category)
         | Q(brand__brand=dropdown_brand) | Q(city__name=dropdown_city))
        if not context['queryset']:
            return render(request, 'empty_index.html', context)
        else:
            return render(request, 'index.html', context)
    if request.GET.get('dropdown_sorted'):
        dropdown_sorted = request.GET.get('dropdown_sorted')
        if dropdown_sorted == 'new':
            context['queryset'] = Products.objects.all().order_by('-create_date')
            return render(request, 'index.html', context)
        if dropdown_sorted == 'old':
            context['queryset'] = Products.objects.all().order_by('create_date')
            return render(request, 'index.html', context)
        if dropdown_sorted == 'price_ascending':
            context['queryset'] = Products.objects.all().order_by('price')
            return render(request, 'index.html', context)
        if dropdown_sorted == 'price_descending':
            context['queryset'] = Products.objects.all().order_by('-price')
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)


@login_required(login_url="/login")
def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'product_card.html', {'product': product})
