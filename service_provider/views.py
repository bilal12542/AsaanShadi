from django.shortcuts import render, redirect , get_object_or_404
from .models import ServiceProvider, Category
from .forms import ServiceForm, CategoryForm , PackageForm
from django.contrib import messages
# Create your views here.


def index(request):
    data = 123
    return render(request, 'service_provider/index.html', {"data":data})

def about(request):
    return render(request, 'service_provider/about_page.html')


def catering(request):
    cat = Category.objects.get(category="Catering")
    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)
    print(context)

    return render(request, 'service_provider/catering.html',context)

def detail_catering(request, id):
    context = {}
    cat = Category.objects.get(category="Catering")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    context["data"] = cat_service.get(id=id)


    # add the dictionary during initialization

    return render(request, "service_provider/detail_view.html", context)


def catering_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    cat = Category.objects.get(category="Catering")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    obj = get_object_or_404(cat_service, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("catering")

    return render(request, "service_provider/delete_view.html", context)


def decorations(request):
    cat = Category.objects.get(category="Decorations")

    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)

    return render(request, 'service_provider/decorations.html',context)

def photography(request):
    cat = Category.objects.get(category="Photography")

    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)

    return render(request, 'service_provider/photography.html',context)

def transport(request):
    cat = Category.objects.get(category="Transport")

    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)

    return render(request, 'service_provider/transport.html',context)


def add_Package(request):
    if request.method == "POST":
        # add the dictionary during initialization
        package_form = PackageForm(request.POST)
        if package_form.is_valid():
            package_form.save()
            messages.success(request, "Successfully added!")
            return redirect("ServiceAdd")
    else:
        package_form = PackageForm()
    return render(request, "service_provider/add_category.html", {'form': package_form})


def add_Cateogry(request):
    if request.method == "POST":
    # add the dictionary during initialization
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Successfully added!")
            return redirect("ServiceAdd")
    else:
        category_form = CategoryForm()
    return render(request, "service_provider/add_category.html", {'form':category_form })


def add_Service(request):

    if request.method == "POST":
    # add the dictionary during initialization
        service_form = ServiceForm(request.POST,request.FILES)
        #print(service_form)
        if service_form.is_valid():
            print("1")
            service_form.save()
            messages.success(request, "Successfully added!")
            return redirect('catering')
        else:
            print(service_form.errors)
    else:
        print("I'm done ")
        service_form = ServiceForm()
    return render(request, "service_provider/add_Service.html", {'form':service_form} )