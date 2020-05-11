"""
Restaurant app URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name='restaurant-homepage'),
    path('detail/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('add/', views.RestaurantCreate.as_view(), name='restaurant-create'),
    path('update/<int:pk>/', views.RestaurantUpdate.as_view(), name='restaurant-update'),
    path('<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurant-delete'),
]
