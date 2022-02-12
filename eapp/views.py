from itertools import product
from platform import python_version_tuple
from tkinter.messagebox import CANCEL
from django.shortcuts import render
import os
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import *
from eapp.models import *
from django.contrib.auth.models import User


def reg(request):
    return render(request, 'index.html')

# Create your views here.


def registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone_no']
        tb = user_tb(name=name, email=email, username=username,
                     password=password, phone_no=phone_no)
        tb.save()
        return render(request, 'registeration.html')
    else:
        return render(request, 'registeration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = user_tb.objects.filter(username=username, password=password)
        for x in user:
            name = x.username
            pwd = x.password
            if username == name and password == pwd:
                request.session['uid'] = x.id
                return render(request, 'index.html', {'success': 'successfuly  login'})
        return render(request, 'login.html', {'error': 'invalid retry'})

    else:

        return render(request, 'login.html')


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
        tb = seller_tb(s_name=s_name, s_email=s_email, s_username=s_username,
                       s_password=s_password, s_phone_no=s_phone_no)
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



def booking(request):
    if request.session.has_key('uid'):
        if request.method =='POST':
            print("sssssssssssssssssssss")
            pid = request.POST['pid']
            userid = request.session['uid']
            bookigdatefrom = request.POST['bookingdatefrom']
            bookigdateto = request.POST['bookingdateto']
            productid = product_tb.objects.get(id=pid)
            user_id = user_tb.objects.get(id=userid)
            proid= product_tb.objects.get(id=pid)
            query=product_tb.objects.all().filter(id=pid)
            for x in query:
                 sid = x.sid
                 tb = booking_tb(bookingdatefrom=bookigdatefrom,bookingdateto=bookigdateto,pid=proid,uid=user_id,sid=sid)
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
        booking_tb.objects.filter(id=bid).update(status="cancelled")
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
        print("dshgsgggsgsgd",username,password)
        seller=seller_tb.objects.filter(s_username=username, s_password=password)
        print(seller,"--------------")
        for x in seller:
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
    if request.session.has_key('sid'):
        product_view=product_tb.objects.all()
        return render(request,'productview.html',{"p":product_view})
    else:
        return render(request,'sellerlogin.html')




def userproductview(request):
    if request.session.has_key('uid'):
        product_view=product_tb.objects.all()
        return render(request,'userproductview.html',{"pro":product_view})
    else:
        return render(request,'login.html')





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
            return HttpResponseRedirect('/product_update/')
    else:
        productid=request.GET['pid']
        tea=product_tb.objects.filter(id=productid)
        return render(request,'productupdate.html',{'productup':tea})




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
                return render(request,'index.html', {'success': 'successfuly  login'})
        return render(request, 'admin/login.html', {'error': 'invalid retry'})

    else:

        return render(request, 'admin/login.html')


def index(request):
    return render(request, 'admin/index.html')


















