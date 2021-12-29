from django.contrib import admin

# Register your models here.
from .models import Package, Category,ServiceProvider, Become_ServiceProvider


admin.site.register(Package)
admin.site.register(Category)
admin.site.register(ServiceProvider)
admin.site.register(Become_ServiceProvider)

