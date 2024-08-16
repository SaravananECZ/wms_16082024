from django.urls import path
from . import views

app_name = 'warehouse_management'

urlpatterns = [
    path('create_warehouse_listings/', views.create_warehouse_listings, name='create_warehouse_listings'),
    path('search/', views.search_view, name='search'),
    path('role-selection/', views.role_selection_view, name='RoleSelection'),  
]