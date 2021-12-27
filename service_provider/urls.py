from django.urls import path
from . import views


urlpatterns = [
    path("" ,views.index, name="HomePage"),
    path("about-us", views.about, name="About-us"),
    path("cateringpage", views.catering, name="catering"),
    path("decorationpage", views.decorations, name="decorations"),
    path("photographypage", views.photography, name="photography"),
    path("transportpage", views.transport, name="transport"),
    path("cateringpage/add_Category", views.add_Cateogry, name="categoryAdd"),
    path("cateringpage/add_Package", views.add_Package, name="PackageAdd"),
    path("cateringpage/add_Service" , views.add_Service,name="ServiceAdd")
]