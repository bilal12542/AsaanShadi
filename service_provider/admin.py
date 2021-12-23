from django.contrib import admin

# Register your models here.
from .models import Photography,Transportation,Decoration,Catering


admin.site.register(Photography)
admin.site.register(Transportation)
admin.site.register(Decoration)
admin.site.register(Catering)

