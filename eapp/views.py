from itertools import product
from django.shortcuts import render
import os
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import *
from eapp.models import *


def reg(request):
    return render(request,'index.html')
# Create your views here.

def registeration(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        phone_no=request.POST['phone_no']
        tb=user_tb(name=name,email=email,username=username,password=password,phone_no=phone_no)
        tb.save()
        return render(request,'registeration.html')
    else:
        return render(request,'registeration.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=user_tb.objects.filter(username=username, password=password)
        for x in user:
            name=x.username
            pwd=x.password
            if username==name and password==pwd:
                request.session['uid']=x.id
                print("ppppppppppppppppppppppppppppp")
                return render(request,'index.html',{'success':'successfuly  login'})
            else:
                print("hi............................................")
                return render(request,'login.html',{'error':'invalid retry'})
     
    else:
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        return render(request,'login.html')


def product_reg(request):
    if request.session.has_key('sid'):
        if request.method=='POST':
            sellerid=request.session['sid']
            u_id=seller_tb.objects.get(id=sellerid)
            p_name=request.POST['p_name']
            dis=request.POST['dis']
            img=request.FILES['img']
            price=request.POST['price']
            tb=product_tb(p_name=p_name,img=img,dis=dis,price=price,sid=u_id)
            tb.save()
            return render(request,'product.html')
        else:
            return render(request,'product.html')

    else:
        return render(request,"sellerlogin.html")


def seller_reg(request):
    if request.method=='POST':
        s_name=request.POST['s_name']
        s_username=request.POST['s_username']
        s_email=request.POST['s_email']
        s_password=request.POST['s_password']
        s_phone_no=request.POST['s_phone_no']
        tb=seller_tb(s_name=s_name,s_email=s_email,s_username=s_username,s_password=s_password,s_phone_no=s_phone_no)
        tb.save()
        return render(request,'seller.html')
    else:
        return render(request,'seller.html')


def sellerupdate(request):
         if request.method=='POST':
            sid=request.POST['sid']
            s_name=request.POST['s_name']
            s_username=request.POST['s_username']
            s_email=request.POST['s_email']
            s_password=request.POST['s_password']
            s_phone_no=request.POST['s_phone_no']
            tb=seller_tb.objects.filter(id=sid).update(s_name=s_name,s_username=s_username,s_email=s_email,s_password=s_password,s_phone_no=s_phone_no)
            tb.save()
            return render(request,'seller_profile.html')
         else:
             sid=request.GET('sid')
             tb=seller_tb.objects.filter(id=sid)
             return render(request,'seller_profile.html',{'seller':tb})






#USER FORIGN KEY


# def uforign(request):
#     if request.session.has_key('uid'):
#         if request.method == "POST":
#             userid=request.session['u_id']
#             u_id=user_tb.objects.get(id=userid)
#             query=booking_tb(uid=u_id)
#             query.save()
            
#             return render(request,'booking.html')
#         else:
#             return render(request,'booking.html')
#     else:
#         return render(request,"login.html")




# seller forignkey

# def sforign(request):
#     if request.session.has_key('sid'):
#         if request.method == "POST":
#             sellerid=request.session['sid']
#             u_id=seller_tb.objects.get(id=sellerid)
#             query=product_tb(sid=u_id)
#             query.save()
#             return render(request,'product.html')
#         else:
#             return render(request,'product.html')
#     else:
#         return render(request,"sellelogin.html")


# def booking(request):
#          if request.session.has_key('uid'):
#              if request.method=='POST':
#                  sellerid=request.session['sid']
#                  userid=request.session['u_id']
#                  seller_id=seller_tb.objects.get(id=sellerid)
#                  u_id=user_tb.objects.get(id=userid)
#                  bookigdatefrom=request.POST['bookingdatefrom']
#                  bookigdateto=request.POST['bookingdateto']
#                  tb=booking_tb(bookingdatefrom=bookigdatefrom,bookingdateto=bookigdateto,uid=u_id,sid=seller_id)
#                  tb.save()
#                  return render(request,'booking.html')
#              else:
#                  return render(request,'booking.html')
#          else:
#              return render(request,"login.html")
#      else:
#         return render(request,"sellerlogin.html")


def seller_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print("dshgsgggsgsgd",username,password)
        seller=seller_tb.objects.filter(s_username=username, s_password=password)
        print(seller,"--------------")
        for x in seller:
            print("for loooooooooooooooooooooooooooop")
            name=x.s_username
            pwd=x.s_password
            if username==name and pwd==password:
                request.session['sid']=x.id
                return render(request,'index.html',{'success':'successfuly  login'})
        return render(request,'sellerlogin.html',{'error':'invalid retry'})
     
    else:
        return render(request,'sellerlogin.html')

def logout(request):
    if request.session.has_key('sid'):
        del request.session['sid']
    if request.session.has_key('uid'):
        del request.session['uid']

    
    return render(request,'index.html')


def productview(request):
    product_view=product_tb.objects.all()
    return render(request,'productview.html',{"p":product_view})




def productupdate(request):
   

    if request.method=='POST':
        pid=request.GET['pid']
        p_name=request.POST['p_name']
        dis=request.POST['dis']
        price=request.POST['price']
        imgup=request.POST['imgupdate']

        if imgup=='Yes':

            image1=request.FILES['imag']
            oldrec=product_tb.objects.all().filter(id=pid)
            updrec=product_tb.objects.get(id=pid)
            for x in oldrec:
                imgurl=x.img.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('Successfully deleted')
            updrec.img=image1
            updrec.save()
        elif imgup=='NO':
            product_tb.objects.filter(id=pid).update( p_name=p_name,dis=dis,price=price)
            return HttpResponseRedirect('/product_view/')
            
       


    else:
            productid=request.GET['pid']
            tea=product_tb.objects.filter(id=productid)
            return render(request,'productupdate.html',{'productup':tea})
















# def foreign(request):
#     if request.session.has_key('user_id'):
#         if request.method == "POST":
#             uid=request.session['user_id']
#             booking_id=user_tb.objects.get(id=uid)
#             query=booking_tb(student_id=booking_id)
#             query.save()
            
#             return render(request,'booking.html')
#         else:
#             return render(request,'booking.html')
#     else:
#         return render(request,"student_login.html")
