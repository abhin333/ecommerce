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
    path('user_update/',views.userupdate),
    path('single/',views.single),
    path('productdlt/',views.productdlt),
    path('ubookingview/',views.ubookingview),
    path('sbookingview/',views.sbookingview),
    path('booking/',views.booking),
    path('userproductview/',views.userproductview),
    path('bookingdlt/',views.bookingdlt),
    path('userbookingcheck/',views.userbookingcheck),
    path('admin-login/',views.adminlogin),
    path('index/',views.index),
    path('userview/',views.userview),
    path('sellerview/',views.sellerview),
    path('adbooking/',views.adbooking),
    path('seller_approve/',views.seller_approve),
    path('sellerapprov/',views.sellerapprov),
    path('seller_disapproval/',views.seller_disapproval),
    path('search/',views.search),



















    # path('booking/',views.booking),


]