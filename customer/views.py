from django.shortcuts import render
from service_provider.models import ServiceProvider
from math import ceil

# Create your views here.
def index(request):
    return render(request, 'index.html')


def show_ServiceProvider(request):
    # context = {}
    # context["dataset"] = ServiceProvider.objects.all()
    # print(context)
    allProds = []
    catprods = ServiceProvider.objects.values('category', 'id')
    #print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = ServiceProvider.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    print(allProds)
    params = {'allProds': allProds}
    return render(request, 'show_ServiceProvider.html', params)