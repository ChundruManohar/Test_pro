from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('get_all_addresses/', views.get_all_addresses, name='get_all_addresses'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete_user, name='delete'),
    
]
