from datetime import datetime


from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from product.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
from product.models import Product, Category, Review
from shop import settings


# Create your views here.

# def hello_view(request):
#     return HttpResponse("Hello, it's my project")
#
#
# def current_date_view(request):
#     current = datetime.now()
#     return HttpResponse(current)
#
#
# def goodbye_view(request):
#     return HttpResponse("Goodbye!!!")

def main_view(request):
    return render(request, 'index.html')


@login_required
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        categories = Category.objects.all()
        selected_category = request.GET.get('category')
        search = request.GET.get('search')
        order = request.GET.get('order')
        if selected_category:
            category = get_object_or_404(Category, title=selected_category)
            products = products.filter(category=category)
        elif search:
            products = products.filter(
                Q(title__icontains=search)
            )
        elif order == 'title':
            products = products.order_by('title')
        elif order == '-title':
            products = products.order_by('-title')
        elif order == 'created_at':
            products = products.order_by('created_at')
        elif order == '-created_at':
            products = products.order_by('-created_at')
        else:
            products = products.exclude(user=request.user)

        max_page = products.__len__() / settings.PAGE_SIZE

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        page = int(request.GET.get('page', 1))

        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE

        products = products[start:end]

        context = {
            "products": products,
            "selected_category": selected_category,
            "categories": categories,
            "pages": range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)



def category_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'products/categories.html', context=context)


def product_detail_view(request, product_id=None):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {
            "product": product,
            'form': ReviewCreateForm()
        }
        return render(request, 'products/products_detail.html', context)
    elif request.method == 'POST':
        form = ReviewCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Review.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/products/{product_id}/')
        context = {
            'form': form,
        }
        return render(request, 'products/products_detail.html', context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm()
        }
        return render(request, 'products/products_create.html', context=context, )
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')
        else:
            context = {
                "form": ProductCreateForm()
            }
            return render(request, 'products/products_create.html', context=context, )


def category_create_view(request):
    if request.method == 'GET':
        context = {
            "form": CategoryCreateForm(),
        }
        return render(request, 'products/categories_create.html', context=context)

    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')
        context = {
            "form": form
        }
        return render(request, 'products/categories_create.html', context=context)

def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm(instance=product)
        }
        return render(request, 'products/product_update.html', context)
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}/')
        return render(request, 'products/product_update.html', {"form": form})

