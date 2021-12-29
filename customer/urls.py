from django.urls import path
from . import views
import service_provider.views

urlpatterns = [
    path('', views.index , name='index'),
    path('ShowServices/' , views.show_ServiceProvider , name='show_ServiceProvider'),
    #path('')
    path('ShowServices/services/dashboard/<int:id>', service_provider.views.details , name='showing_ServiceProvider')
]