from django.http import request
from django.urls import path
from eapp import views

urlpatterns=[
    path('',views.reg),
    path('registeration/',views.registeration),
    path('login/',views.login),
    path('logout/',views.logout),
    path('product_reg/',views.product_reg),
    path('seller_reg/',views.seller_reg),
    path('seller_login/',views.seller_login),
    path('productview/',views.productview),
    path('product_update/',views.productupdate),
    path('seller_update/',views.sellerupdate),



    # path('booking/',views.booking),


]