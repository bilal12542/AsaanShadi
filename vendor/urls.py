from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                    path('', views.user_login, name='login'),
                  path('become-vendor/', views.become_vendor, name='become-vendor'),
                  path('dashboard/', views.vendor_dashboard, name='dashboard'),
                  path('add-product/', views.add_product, name='add-product'),
                  path('view-product/', views.view_product, name='view-product'),
                  path('become-vendor/', views.become_vendor, name='become-vendor'),

                  path('<slug:category_slug>/<slug:product_slug>/', views.single_product, name='single-product'),
                  path('logout/', views.logout_vendor, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
