from django.http import request
from django.urls import path
from eapp import views


urlpatterns=[
    path('',views.reg),
    path('shop/',views.shop),
    path('registeration/',views.registeration),
    path('login/',views.login),
    path('logout/',views.logout),
    path('product_reg/',views.product_reg),
    path('seller_reg/',views.seller_reg),
    path('seller_login/',views.seller_login),
    path('productview/',views.productview),
    path('contact/',views.contact),
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
    path('userforgotpass/',views.userforgotpass),
    path('seller_approve/',views.seller_approve),
    path('sellerapprov/',views.sellerapprov),
    path('seller_disapproval/',views.seller_disapproval),
    path('search/',views.search),
    path('seller_dlt/',views.seller_dlt),
    path('view/',views.view),
    path('views/',views.views),
    path('forgotpass_seller/',views.forgotpass),
    path('confirmation_seller/',views.confirmation_seller),
    path('confirmation_user/',views.confirmation_user),
    path('changepass/',views.changepassword),
    path('mailchecking/',views.mailchecking),
    path('mailcheckingg/',views.mailcheckingg),

    path('changepassword2/',views.changepassword2),



   

 
















    # path('booking/',views.booking),


]
