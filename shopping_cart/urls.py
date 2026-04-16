# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from . import views 

# Define URL patterns
urlpatterns = [
    path('home/', views.home, name="recipes"),  # Home page
    path("admin/", admin.site.urls),        
    path('login/', views.login_page, name='login_page'),    # Login page
    path('register/', views.register_view, name='register'),
    path('about/', views.about, name="about"),
    
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    
     path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    
     path('logout/', views.logout_view, name='logout'),
    
]

# Serve media files if DEBUG is True (development mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()