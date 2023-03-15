from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('products/<int:id>', views.products),
    path('customers/', views.Customer.as_view() ),
    path('customers/<int:id>', views.Customer.as_view() ),
    path('login/', views.MyTokenObtainPairView.as_view()),
    
]
