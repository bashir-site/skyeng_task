from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import ProductForm, UserRegistrationForm
from .models import Product, Category


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Успешно вошли в систему.')
            return redirect('/')  # Redirect to a 'home' view or any other view
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Успешно вышли из системы.')
    return redirect('/')


@login_required
def see(request):
    products = Product.objects.all()
    return render(request, 'products/see.html', {'products': products})


@login_required
def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    return render(request, 'products/add.html', {'form': form})


@login_required
def edit(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    return render(
        request, 'products/edit.html',
        {'product': product, 'categories': categories}
    )


@login_required
def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'products/edit.html', {'product': product})


@login_required
def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")
