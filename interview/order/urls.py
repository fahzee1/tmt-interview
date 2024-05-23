
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, ListOrdersByDateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('orders/by-date/', ListOrdersByDateView.as_view(), name='list-orders-by-date'),

]