from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.logout_vendor, name='logout'),
    path('become-ServiceProvider/', views.become_ServiceProvider, name='become-ServiceProvider'),
    path("dashboard/" ,views.index, name="HomePage"),
    path("dashboard/<int:id>/" ,views.details, name="HomePage"),
    path("about-us", views.about, name="About-us"),
    path("cateringpage/", views.catering, name="catering"),
    path("cateringpage/add_Category/", views.add_Cateogry, name="categoryAdd"),
    path("cateringpage/<int:id>/", views.detail_catering, name="detail-catering"),
    path('cateringpage/<int:id>/delete/', views.catering_delete_view, name= "delete-catering"),
    path('cateringpage/<int:id>/update/', views.update_Service, name= "update-catering"),
    path("decorationpage/", views.decorations, name="decorations"),
    path("decorationpage/<int:id>/", views.detail_decorations, name="detail-decorations"),
    path('decorationpage/<int:id>/delete/', views.decorations_delete_view, name= "delete-decorations"),

    path("photographypage/", views.photography, name="photography"),
    path("photographypage/<int:id>/", views.detail_photography, name="detail-photography"),
    path('photographypage/<int:id>/delete/', views.photography_delete_view, name="delete-photography"),

    path("transportpage/", views.transport, name="transport"),
    path("transportpage/<int:id>/", views.detail_transport, name="detail-transport"),
    path('transportpage/<int:id>/delete/', views.transport_delete_view, name="delete-transport"),


    path("cateringpage/add_Package", views.add_Package, name="PackageAdd"),
    path("cateringpage/add_Service" , views.add_Service,name="ServiceAdd")
]