from django.urls import path
from .views import (CustomerListCreateView, CustomerRetrieveUpdateDestroyView,
                    ServiceListCreateView, ServiceRetrieveUpdateDestroyView,
                    OrderListCreateView, OrderRetrieveUpdateDestroyView,OrderHistoryView)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroyView.as_view(), name='service-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('orders/history/',OrderHistoryView.as_view(), name= 'order-history')
]
