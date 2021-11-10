from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customer/<int:id>',views.customer,name='customer_show'),
    path('product/',views.product,name='product'),
    path('order/create/',views.orderCreate,name='order.create'),
    path('order/update/<int:orderId>',views.orderUpdate,name='order.update'),
    path('order/delete/<int:orderId>',views.orderDelete,name='order.delete'),
]
