from django.db import models

class  user_tb(models.Model):
    name=models.CharField(max_length=100,default="")
    username=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
    phone_no=models.CharField(max_length=100,default="")
   
   

class seller_tb(models.Model):
    s_name=models.CharField(max_length=10,default="")
    s_username=models.CharField(max_length=10,default="")
    s_password=models.CharField(max_length=10,default="")
    s_email=models.CharField(max_length=10,default="")
    s_phone_no=models.CharField(max_length=10,default="")

class product_tb(models.Model):

    sid=models.ForeignKey(seller_tb, on_delete=models.CASCADE)
    p_name=models.CharField(max_length=10,default="")
    dis=models.CharField(max_length=100,default="")
    price=models.CharField(max_length=10000,default="")
    img=models.FileField(upload_to='images',default='')
   
   
    



class booking_tb(models.Model):
    bookingdatefrom=models.DateField(max_length=100,default="")
    bookingdateto=models.DateField(max_length=100,default="")
    pid=models.ForeignKey(product_tb,on_delete=models.CASCADE)
    uid=models.ForeignKey(user_tb,on_delete=models.CASCADE)
    sid=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default="")

   
   
