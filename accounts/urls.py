from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customer/<int:id>',views.customer,name='customer_show'),
    path('product/',views.product,name='product'),
]
