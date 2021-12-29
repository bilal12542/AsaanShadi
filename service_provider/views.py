from django.shortcuts import render, redirect , get_object_or_404
from .models import ServiceProvider, Category , Become_ServiceProvider
from .forms import ServiceForm, CategoryForm , PackageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect('HomePage')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HomePage')

            else:
                print("Someone tried to login and failed.")
                return redirect('/')
        except Exception as identifier:
            print(identifier)
            return redirect('/')

    else:
        return render(request, 'ServiceProvider_login/login.html')

@login_required
def logout_vendor(request):
    logout(request)
    return redirect('login')


def become_ServiceProvider(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            serviceprovider = Become_ServiceProvider.objects.create(owner_name=user.username, created_by=user)
            serviceprovider.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'ServiceProvider_login/become_serviceprovider.html', {'form': form})


@login_required(login_url='login')
def index(request):
    context = {}
    context["dataset"] = ServiceProvider.objects.all()
    print(context)
    return render(request, 'service_provider/index.html', context)

def details(request, id):
    context = {}
    # cat =
    # cat_service = ServiceProvider.objects.filter(category=cat.id)
    context["data"] = ServiceProvider.objects.filter(id=id)
    a = ServiceProvider.objects.filter(id=id)
    print(a)
    # for i in a:
    #     print(i.location)
    #print(a.location)


    # add the dictionary during initialization

    return render(request, "service_provider/details.html", context)

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


def detail_decorations(request, id):
    context = {}
    cat = Category.objects.get(category="Decorations")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    context["data"] = cat_service.get(id=id)


    # add the dictionary during initialization

    return render(request, "service_provider/detail_view.html", context)

def decorations_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    cat = Category.objects.get(category="Decorations")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    obj = get_object_or_404(cat_service, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("catering")

    return render(request, "service_provider/delete_view.html", context)


def photography(request):
    cat = Category.objects.get(category="Photography")

    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)

    return render(request, 'service_provider/photography.html',context)


def detail_photography(request, id):
    context = {}
    cat = Category.objects.get(category="Photography")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    context["data"] = cat_service.get(id=id)


    # add the dictionary during initialization

    return render(request, "service_provider/detail_view.html", context)

def photography_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    cat = Category.objects.get(category="Photography")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    obj = get_object_or_404(cat_service, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("catering")

    return render(request, "service_provider/delete_view.html", context)

def transport(request):
    cat = Category.objects.get(category="Transport")

    context = {}
    context["dataset"] = ServiceProvider.objects.filter(category=cat.id)

    return render(request, 'service_provider/transport.html',context)

def detail_transport(request, id):
    context = {}
    cat = Category.objects.get(category="Transport")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    context["data"] = cat_service.get(id=id)


    # add the dictionary during initialization

    return render(request, "service_provider/detail_view.html", context)

def transport_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    cat = Category.objects.get(category="Transport")
    cat_service = ServiceProvider.objects.filter(category=cat.id)
    obj = get_object_or_404(cat_service, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("catering")

    return render(request, "service_provider/delete_view.html", context)


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
            service_form.save()
            messages.success(request, "Successfully added!")
            return redirect('catering')
        else:
            print(service_form.errors)
    else:
        service_form = ServiceForm()
    return render(request, "service_provider/add_Service.html", {'form':service_form} )

def update_Service(request,id):
    # or "Decortaions" or "Photography" or "Transport"
    # cat = Category.objects.get(category="Catering" )
    # cat_service = ServiceProvider.objects.filter(category=cat.id)
    obj = get_object_or_404(ServiceProvider, id=id)
    #print(cat)

    print(obj.location)
    context = {}
    # add the dictionary during initialization
    service_form = ServiceForm(request.POST or None, request.FILES or None , instance = obj)
    print(service_form)
    if service_form.is_valid():
        service_form.save()
        messages.success(request, "Successfully Updated!")
        return redirect('HomePage')
    else:
        pass
        #print(service_form.errors)
    context["form"] = service_form
    return render(request, "service_provider/new_update.html", context )