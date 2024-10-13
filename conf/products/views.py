from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm


def see(request):
    products = Product.objects.all()
    return render(request, 'products/see.html', {'products': products})


def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ProductForm()

    return render(request, 'products/add.html', {'form': form})


def edit(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    return render(request, 'products/edit.html', {'product': product, 'categories': categories})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'products/edit.html', {'product': product})


def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")

