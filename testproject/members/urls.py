from django.urls import path 
from . import views
from django.http import HttpResponse

from django.contrib import admin
from django.urls import path, include
 
from django.urls import path

# from .views import member_create_view
 
# urlpatterns = [ 
# ] 

urlpatterns = [
    path('members/', views.members, name='members'), 
    path('', views.members, name='members'),
    path('insert', views.submit_member, name='submit_member'),

   
    # path('success', lambda request: HttpResponse("Member saved successfully!")),
    path('show/', views.show_members, name='show'), 
    path('update/<int:id>/', views.update_member, name='update'),
    path('update/<int:id>/', views.update_member, name='update'),
    path('delete/<int:id>/', views.delete_member, name='delete_member'),
    path('logout/', views.logout_view, name='logout')  

    

]