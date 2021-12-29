from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('become-vendor/', views.become_vendor, name='become-vendor'),
                  path('dashboard/', views.vendor_dashboard, name='dashboard'),
                  path('add-product/', views.add_product, name='add-product'),
                  path('view-product/', include(
                      [
                          path('', views.view_product, name='view-product'),
                          path('<slug:category_slug>/<slug:product_slug>/', include(
                              [
                                  path('view/', views.single_product, name='single-product'),
                                  path('edit/', views.edit_product, name='edit-product'),
                                  path('delete/', views.delete_product, name='delete-product')
                              ]
                          )),
                      ]
                  )),
                  path('become-vendor/', views.become_vendor, name='become-vendor'),
                  path('', views.user_login, name='login'),
                  path('logout/', views.logout_vendor, name='logout'),
                  path('<slug:category_slug>/<slug:product_slug>/', views.view_customer_product_single,
                       name='view-customer-product-single'),
                  path('products/', views.view_customer_product, name='view-customer-product')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
