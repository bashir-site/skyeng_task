from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})


def add_new_product(request):
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

    return render(request, 'products/add_new_product.html', {'form': form})
