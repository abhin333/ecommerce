import base64
from email import message
from itertools import product
from platform import python_version_tuple
import re
from tkinter.messagebox import CANCEL
from django.shortcuts import render
import os
from django.http.response import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.http import *
from eapp.models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
import random
import string
import hashlib
from cryptography.fernet import Fernet 


# Create your views here.

def reg(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
    
    


def registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone_no']
        hashpass = hashlib.md5(password.encode('utf8')).hexdigest()
        message = f'thank you for register our website  as a user'
        subject = 'camera rent'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail(subject,message,email_from,recipient_list) 
        tb = user_tb(name=name, email=email, username=username,password=hashpass, phone_no=phone_no)
        tb.save()
        return render(request, 'registeration.html')
    else:
        return render(request, 'registeration.html')


def view(request):
    username = request.GET['username']
    b = user_tb.objects.filter(username=username)  #Store the name, if there is a same name exist in the database
    if b:
        msg = {"Message":"Username already Taken"}
    else:
        msg = {"Message": "Username available"}
    return JsonResponse(msg)


def views(request):
    username = request.GET['username']
    print("sdbyuysfd")
    b = seller_tb.objects.filter(s_username=username)  #Store the name, if there is a same name exist in the database
    if b:
        msg = {"Message":"Username already Taken"}
    else:
        msg = {"Message": "Username available"}
    return JsonResponse(msg)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        hashpass = hashlib.md5(password.encode('utf8')).hexdigest()
        user = user_tb.objects.filter(username=username, password=hashpass)
        if user:
            for x in user:
                name = x.username
                pwd = x.password
            if username == name and pwd == hashpass:
                request.session['uid'] = x.id
                print(username,password)
                return render(request, 'index.html', {'success': 'successfuly  login'}) 
            else:
                return render(request, 'login.html', {'error': 'invalid retry'})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



#user password chainging............
def changepassword2(request):
    if request.session.has_key('uid'):
        if request.method=='POST':
            oldpassword=request.POST['oldpassword']
            newpass=request.POST['newpass']
            uid=request.session['uid']
            hashpas= hashlib.md5(oldpassword.encode('utf8')).hexdigest()
            hashpass = hashlib.md5(newpass.encode('utf8')).hexdigest()
            tb=user_tb.objects.filter(id=uid)
            for x in tb:
                oldpass=x.password
                if oldpass== hashpas :
                     user_tb.objects.filter(id=uid).update(password=hashpass)
                     return render(request,'changepassword2.html',{'success':"password changed"})
                else:
                    return render(request,'changepassword2.html',{'error':"old password is not correct"})
        else: 
            return render(request,'changepassword2.html')
    else:
        return render(request,'login.html')



#-------------------------------------




def product_reg(request):
    if request.session.has_key('sid'):
        if request.method == 'POST':
            sellerid = request.session['sid']
            u_id = seller_tb.objects.get(id=sellerid)
            p_name = request.POST['p_name']
            dis = request.POST['dis']
            img = request.FILES['img']
            price = request.POST['price']
            tb = product_tb(p_name=p_name, img=img,dis=dis, price=price, sid=u_id)
            tb.save()
            return render(request, 'product.html')
        else:
            return render(request, 'product.html')

    else:
        return render(request, "sellerlogin.html")


def seller_reg(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_username = request.POST['s_username']
        s_email = request.POST['s_email']
        s_password = request.POST['s_password']
        s_phone_no = request.POST['s_phone_no']
        hashpass = hashlib.md5(s_password.encode('utf8')).hexdigest()
        message = f'thank you for register our website as a seller '
        subject = 'camera rent'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [s_email, ] 
        send_mail(subject,message,email_from,recipient_list) 
        tb = seller_tb(s_name=s_name, s_email=s_email, s_username=s_username,s_password=hashpass, s_phone_no=s_phone_no,authN="pending")
        tb.save()
        return render(request, 'seller.html')
    else:
        return render(request, 'seller.html')


def sellerupdate(request):

    if request.session.has_key('sid'):
         if request.method == 'POST':
            sellerid = request.session['sid']
            s_name = request.POST['s_name']
            s_username = request.POST['s_username']
            s_email = request.POST['s_email']
            s_phone_no = request.POST['s_phone_no']
            t = seller_tb.objects.filter(id=sellerid).update(s_name=s_name,s_username=s_username,s_email=s_email,s_phone_no=s_phone_no)
            tb = seller_tb.objects.filter(id=sellerid)
            return render(request,'seller_profile.html',{'seller':tb})
         else:
            sellerid = request.session['sid']
            tb = seller_tb.objects.filter(id=sellerid)
            return render(request,'seller_profile.html',{'seller':tb})
    else:
        return render(request,'sellerlogin.html')


def forgotpass(request):
    if request.method=='POST':
        f_email = request.POST['f_email']
        tb = seller_tb.objects.filter(s_email=f_email)
        for x in tb:
            email=x.s_email
            if email==f_email:
                 ss=encrypt(x.id)
                 message = f'please click this link and reset your password :http//:127.0.0.1:8000/confirmation_seller/?sid={ss}'
                 subject = 'welcome to Whats App'
                 email_from = settings.EMAIL_HOST_USER 
                 recipient_list = [f_email, ] 
                 print(recipient_list)
                 send_mail( subject,message, email_from, recipient_list) 
                 b = seller_tb(s_email=f_email)
                 b.save()
                 return render(request,'forgotpassword.html') 
            else:
                 return render(request,"forgotpassword.html") 
    else:
        return render(request,"forgotpassword.html") 


def confirmation_seller(request):
    if request.method=='POST':
        print("-------------------------")
        s_password = request.POST['s_password']
        newpassword=request.POST['cs_password']
        hashpass = hashlib.md5(newpassword.encode('utf8')).hexdigest()
        sid=request.GET['sid']

        print("888888888888888888888888888888")

        print("99999999999999999999999999999999999999999999")
        if s_password==newpassword:
            message = f'Your password is channged'
            subject = 'camera rent'
            email_from = settings.EMAIL_HOST_USER 
            tb=seller_tb.objects.filter(id=sid)
            for x in tb:
                email=x.s_email
            recipient_list = [email, ] 
            send_mail(subject,message,email_from,recipient_list) 
            seller_tb.objects.filter(id=sid).update(s_password=hashpass)
            return HttpResponseRedirect('/')
        else:
            return render(request,"confirmpassseller.html",{'errorrr':'password are not same please re enter the passsword'})
    else:
        print("=========================") 
        sid=request.GET['sid']
        sid=decrypt(sid)
        query=seller_tb.objects.filter(id=sid)
        return render(request,'confirmpassseller.html',{'query':query})



# link cryptography code


def encrypt(txt):
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk*************************")
        return encrypted_text


def decrypt(txt):
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        txt = base64.urlsafe_b64decode(txt)
        print(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
        return decoded_text



def changepassword(request):
    if request.session.has_key('sid'):
        if request.method=='POST':
            oldpassword=request.POST['oldpassword']
            newpass=request.POST['newpass']
            sid=request.session['sid']
            hashpas= hashlib.md5(oldpassword.encode('utf8')).hexdigest()
            hashpass= hashlib.md5(newpass.encode('utf8')).hexdigest()
            tb=seller_tb.objects.filter(id=sid)
            for x in tb:
                oldpass=x.s_password
                if oldpass==hashpas :
                     seller_tb.objects.filter(id=sid).update(s_password=hashpass)
                     return render(request,'changepassword.html',{'success':"password changed"})
                else:
                    return render(request,'changepassword.html',{'error':"old password is not correct"})
        else: 
            return render(request,'changepassword.html')
    else:
        return render(request,'seller_login.html')

def mailchecking(request):
    mail= request.GET['a']
    print(mail)
    print("---------------------------------------------------")
    b = seller_tb.objects.filter(s_email=mail)  #Store the name, if there is a same name exist in the database
    if b:
        msg = {"Message":"TRUE"}
    else:
        msg = {"Message":"FALSE"}
    return JsonResponse(msg)


# def mail_sender(subject,message, recipient):
# 	email_from =  settings.EMAIL_HOST_USER 
# 	recipient_list = [recipient, ] 
# 	send_mail( subject, message, email_from, recipient_list ) 



# def mailmessage(request):
#     if request.method=='POST':
#         s_email=request.POST['f_email']
#         subject = 'welcome to Whats App'
#         usermessage = f'please click this link and reset your password :"http//:127.0.0.0.1:8001/?sid={{x.sid}}"'
#         mail_sender("message recieved", usermessage,s_email)
#         mail_sender("tindertapp@gmail.com")
#         return render(request,"frontend/contact.html")		
#     else:
#         return render(request,"frontend/contact.html")
            
            


def userupdate(request):

    if request.session.has_key('uid'):
        print("---------------1")
        if request.method == 'POST':
            print("________________2")
            userid=request.session['uid']
            name=request.POST['name']
            username=request.POST['username']
            email=request.POST['email']            
            phone_no=request.POST['phone_no']
            print(userid,name,username,email,phone_no)
            t = user_tb.objects.all().filter(id=userid).update(name=name, username=username,email=email,phone_no=phone_no)

            print('ppppppppppppppppppppppppppppppppppppppppppppp')
            tb=user_tb.objects.filter(id=userid)
            return render(request, 'user_profile.html',{'user':tb})
        else:
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            userid=request.session['uid']
            tb=user_tb.objects.filter(id=userid)
            return render(request, 'user_profile.html', {'user': tb})
    else:
        return render(request, 'login.html')


def single(request):
    if request.session.has_key('uid'):
        pid = request.GET['pid']
        product_view = product_tb.objects.filter(id=pid)
        return render(request, 'single.html', {"pro": product_view})
    else:
        return render(request, 'sellerlogin.html')



def view(request):
    username= request.GET['username']
    print(username)
    print("---------------------------------------------------")
    b = user_tb.objects.filter(username=username)  #Store the name, if there is a same name exist in the database
    if b:
        msg = {"Message":"Username already Taken"}
    else:
        msg = {"Message": "Username available"}
    return JsonResponse(msg)



def booking(request):
    if request.session.has_key('uid'):
        if request.method =='POST':
            print("sssssssssssssssssssss")
            pid = request.POST['pid']
            userid = request.session['uid']
            bookingdatefrom = request.POST['bookingdatefrom']
            bookingdateto = request.POST['bookingdateto']
            productid = product_tb.objects.get(id=pid)
            user_id = user_tb.objects.get(id=userid)
            proid= product_tb.objects.get(id=pid)
            query=product_tb.objects.all().filter(id=pid)
            for x in query:
                 sid = x.sid     
                #  price=int(x.price)/7
                #  print(price,"666666666666666")
                #  l=bookingdateto
                #  f=bookingdatefrom
                #  k=l-f
                #  p=k*price
                #  print(p,"ooooooooooooooooooooooooooo")
                #  print(k,"jjjjjj")  
                 tb = booking_tb(bookingdatefrom=bookingdatefrom,bookingdateto=bookingdateto,pid=proid,uid=user_id,sid=sid)
                 print("kkkkkkkkkkkkkkkkkkkkkkkk")
                 tb.save()
                
                 return HttpResponseRedirect('/ubookingview/')
        else:
                 productid = request.GET['pid']
                 pd = product_tb.objects.filter(id=productid)
                 return render(request, 'booking.html',{'pro':pd})
       
    else:
        return render(request,"login.html")


def bookingdlt(request):
    if request.session.has_key('uid'):
        bid=request.GET['bid']
        booking_tb.objects.filter(id=bid).delete()
        return HttpResponseRedirect('/ubookingview/')
    else:
        return render(request,'login.html')


def userbookingcheck(request):
    print("************************************* ")
    if request.session.has_key('uid'):
      fdate=request.GET.get('a')
      tdate=request.GET.get('z')
      vv=request.GET.get('c')
      print("lllllllllllllll",vv)
      prodtid=booking_tb.objects.filter(pid=vv)
      print("ggggggggggg",prodtid)
      if prodtid.exists():
          if prodtid.raw('SELECT a.* FROM (SELECT * FROM eapp_booking_tb WHERE pid_id=%s )a WHERE %s BETWEEN bookingdatefrom AND  bookingdateto',[vv,fdate]):
             print("2")
             jj ="t"
             t={'cc': jj} 
             return JsonResponse(t)
          elif prodtid.raw('SELECT a.* FROM (SELECT * FROM eapp_booking_tb WHERE pid_id=%s )a WHERE %s BETWEEN bookingdatefrom AND  bookingdateto',[vv,tdate]):  
             print("3")           
             jj ="t"
             t={'cc': jj} 
             return JsonResponse(t)
          else:
                print("4")
                jj="f"
                t={'cc': jj}                
                return JsonResponse(t)
      else:
                print("5")
                jj="f"
                t={'cc': jj}                
                return JsonResponse(t)
    else:
        return render(request,'sellerlogin.html')







def seller_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        hashpass = hashlib.md5(password.encode('utf8')).hexdigest()
        print("dshgsgggsgsgd",username,hashpass)
        seller=seller_tb.objects.filter(s_username=username,s_password=hashpass,authN='Approved')
        print(seller)
        if seller:
            for x in seller:
                name=x.s_username
                pwd=x.s_password
               
            if username==name and pwd==hashpass:    
                request.session['sid'] = x.id
                return render(request,'index.html',{'success':'successfuly  login'})
            else:
                return render(request,'sellerlogin.html',{'error':'invalid retry'})
        else:
            return render(request,'sellerlogin.html',{'app':'please wait admin is not approved'})
    else:
        return render(request,'sellerlogin.html')

def logout(request):
    if request.session.has_key('sid'):
        del request.session['sid']
    elif request.session.has_key('uid'):
        del request.session['uid']
    elif request.session.has_key('aid'):
        del request.session['aid']
    return render(request,'index.html')


def productview(request):
    if request.session.has_key('sid'):
        product_view=product_tb.objects.all()
        return render(request,'productview.html',{"p":product_view})
    elif request.session.has_key('aid'):
        product_view=product_tb.objects.all()
        return render(request,'productview.html',{"p":product_view})
    else:
        return render(request,'sellerlogin.html')




def userproductview(request):
    if request.session.has_key('uid'):
        product_view=product_tb.objects.all()
        paginator = Paginator(product_view,2) 
        page = request.GET.get('page')
        p = paginator.get_page(page)
        # return render(request,'userviewproduct.html', {"pro": p}
        return render(request,'userproductview.html',{"pro":p})
    else:
        return render(request,'login.html')





def productupdate(request):
    if request.session.has_key('sid'):
        if request.method=='POST':
            pid=request.GET['pid']
            p_name=request.POST['p_name']
            dis=request.POST['dis']
            price=request.POST['price']
            imgup=request.POST['imgupdate']
            if imgup=='YES':
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
            # return HttpResponseRedirect('/productview/')
        # elif imgup=='NO':
            product_tb.objects.filter(id=pid).update( p_name=p_name,dis=dis,price=price)
            return HttpResponseRedirect('/productview/')
        else:
            productid=request.GET['pid']
            tea=product_tb.objects.filter(id=productid)
            return render(request,'productupdate.html',{'productup':tea})
    else:
        return HttpResponseRedirect("/seller_login/")



def productdlt(request):
    if request.session.has_key('sid'):
        pid=request.GET['pid']
        productid=product_tb.objects.all().filter(id=pid).delete()
        return HttpResponseRedirect('/productview/')
    else:
        return render(request,'sellerlogin.html')


def ubookingview(request):
    if request.session.has_key('uid'):
        uid=request.session['uid']
        bview=booking_tb.objects.filter(uid=uid)
        # for x in bview:
        #     price=int(x.pid.price)/7
        #     print(price,"666666666666666")
        #     l=x.bookingdateto
        #     f=x.bookingdatefrom
        #     k=l-f
        #     p=k*price
        #     print(p,"ooooooooooooooooooooooooooo")
        #     print(k,"jjjjjj")   
        return render(request,'ubookingview.html',{"b":bview})
    else:
        return render(request,'login.html')


def sbookingview(request):
    if request.session.has_key('sid'):
        sid=request.session['sid']
        bview=booking_tb.objects.filter(sid=sid)
        return render(request,'sbookingview.html',{"bs":bview})
    else:
        return render(request,'sellerlogin.html')
        
        



def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password)
        for x in user:
            name = x.username
            pwd = x.password
            if username == name and password == pwd:
                request.session['aid'] = x.id
                return render(request,'admin/index.html', {'success': 'successfuly  login'})
        return render(request, 'admin/login.html', {'error': 'invalid retry'})

    else:

        return render(request, 'admin/login.html')


def index(request):
    return render(request, 'admin/index.html')

def userview(request):
    if request.session.has_key('aid'):
        user=user_tb.objects.all()
        return render(request,'admin/userdetails.html',{"usr":user})
    else:
        return render(request,'admin/login.html')


def sellerview(request):
    if request.session.has_key('aid'):
        sellerview=seller_tb.objects.all()
        return render(request,'admin/sellerdetails.html',{"sellerr":sellerview})
    else:
        return render(request,'admin/login.html')

def adbooking(request):
     if request.session.has_key('aid'):
         book=booking_tb.objects.all()
         return render(request,'admin/bookingdetails.html',{'book':book})
     else:
        return render(request,'admin/login.html')


def seller_approve(request):
     if request.session.has_key('aid'):
        sid= request.GET['sid']
        seller_tb.objects.filter(id=sid).update(authN='Approved')
        return HttpResponseRedirect('/sellerapprov/')
     else:
         return render(request, 'admin/login.html',{'msg':'please login'})

def sellerapprov(request):
    if request.session.has_key('aid'):
        sellerview=seller_tb.objects.all()
        return render(request,'admin/approval.html',{"approvall":sellerview})
    else:
        return render(request,'admin/login.html')


def seller_disapproval(request):
    if request.session.has_key('aid'):
        sid=request.GET['sid']
        sellertb=seller_tb.objects.filter(id=sid).delete()
        return HttpResponseRedirect("/sellerapprov/")
    else:
        return render(request,'admin/login.html')




def seller_dlt(request):
    if request.session.has_key('aid'):
        sid=request.GET['sid']
        sellertb=seller_tb.objects.filter(id=sid).delete()
        return HttpResponseRedirect("/sellerview/")
    else:
        return render(request,'admin/login.html')


def search(request):
    if request.method=='POST':
        search_term = request.POST['search']
        product = product_tb.objects.all().filter(p_name__icontains=search_term) 
        return render(request, 'userproductview.html', {'pro' : product, 'search_term': search_term })
    else:
        return render(request, 'userproductview.html')





    
        

    
    




















