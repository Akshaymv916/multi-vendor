from django.urls import path
from .views import OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView, OrderDeleteView, OrderStatusUpdateView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/<int:order_id>/update-status/', OrderStatusUpdateView.as_view(), name='update-order-status'),

]
