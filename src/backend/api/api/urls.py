# backend/api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListAPIView.as_view(), name='item-list'),
    path('transactions/', views.TransactionListAPIView.as_view(),
         name='transaction-list'),
    path('employees/', views.EmployeeListAPIView.as_view(), name='employee-list'),
]
