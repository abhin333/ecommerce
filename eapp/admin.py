from django.contrib import admin

from eapp.models import *

admin.site.register(user_tb)
admin.site.register(seller_tb)
admin.site.register(product_tb)
admin.site.register(booking_tb)