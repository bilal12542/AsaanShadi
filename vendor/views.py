from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .form import AddProduct, ImageForm
from .models import Images
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor, Product
from django.contrib.auth.decorators import login_required
import random


# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                print("Someone tried to login and failed.")
                return redirect('/')
        except Exception as identifier:
            print(identifier)
            return redirect('/')

    else:
        return render(request, 'vendor_login/login.html')


@login_required
def logout_vendor(request):
    logout(request)
    return redirect('login')


def become_vendor(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            vendor = Vendor.objects.create(owner_name=user.username, created_by=user)
            vendor.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'vendor_login/become_vendor.html', {'form': form})


@login_required(login_url='login')
def vendor_dashboard(request):
    vendor = request.user.vendor
    return render(request, 'vendor_login/dashboard.html', {'vendor': vendor})


@login_required
def add_product(request):
    ImageSet = modelformset_factory(Images,
                                    form=ImageForm, extra=3)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddProduct(request.POST, request.FILES)
        formset = ImageSet(request.POST, request.FILES,
                           queryset=Images.objects.none())
        # check whether it's valid:
        if form.is_valid() and formset.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            post_form = form.save(commit=False)
            post_form.vendor = request.user.vendor
            post_form.slug = slugify(post_form.title)
            post_form.thumbnail = None
            post_form.save()
            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(product_id=post_form, image=image)
                    photo.save()
            # redirect to a new URL:
            return redirect("dashboard")
        else:
            print(form.errors, formset.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddProduct()
        formset = ImageSet(queryset=Images.objects.none())
    return render(request, 'vendor_product/add_product.html', {'form': form, 'formset': formset})


def view_product(request):
    products = request.user.vendor.products.all()
    return render(request, 'vendor_product/view_product.html', {'products': products})


def single_product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    images = Images.objects.filter(Q(product_id=product))

    return render(request, 'vendor_product/single_product.html',
                  {'product': product, 'image': images})


def edit_product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    # create a form instance and populate it with data from the request:
    form = AddProduct(request.POST or None, request.FILES or None, instance=product)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        post_form = form.save(commit=False)
        post_form.vendor = request.user.vendor
        post_form.slug = slugify(post_form.title)
        if post_form.image == '':
            post_form.thumbnail = None
        post_form.save()
        # redirect to a new URL:
        return redirect("view-product")
    else:
        print(form.errors)
    # if a GET (or any other method) we'll create a blank form

    return render(request, 'vendor_product/edit_product.html', {'form': form})


def delete_product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    product.delete()
    return redirect('view-product')


def view_customer_product_single(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    images = Images.objects.filter(Q(product_id=product))
    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    return render(request, 'view_customer_product_single.html',
                  {'product': product, 'similar_products': similar_products, 'image': images})

def view_customer_product(request):
    products = Product.objects.all()
    return render(request, 'view_customer_product.html', {'products': products})
