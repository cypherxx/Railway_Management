from django.shortcuts import render,redirect,HttpResponse,Http404,HttpResponsePermanentRedirect
import cx_Oracle
from django.db import connection
from .models import TrainVkp1,BogieVkp1,BookingsVkp4,StationVkp1,RouteStationVkp1,RouteVkp1,SeatVkp1
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.contrib import messages
import random
def index(request):
    return render(request,'HTML/index.html')

def train_details(request):
    return render(request,'HTML/get_train_details.html')

def book_seat(request):
    return render(request,'HTML/booking.html')

def details_of_train(request):
    
            i=request.POST.get('query')
            conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
            cur=conn.cursor()
            myvar3= cur.var(cx_Oracle.CURSOR)
            print(i)
            cur.callfunc('get_train_details',myvar3,[i])
            train_list2=myvar3.getvalue().fetchall()
            train_list2=list(sum(train_list2,()))
            myvar2= cur.var(cx_Oracle.CURSOR)
            print(train_list2)
            s=train_list2[0]
            cur.callfunc('get_train_route',myvar2,[s])
            t=myvar2.getvalue().fetchall()
            c=cur.var(int)
            cur.callproc('seat_avail',[i,c])
            train_info_list=list(sum(t, ()))
            train_list2.append(train_info_list)
            train_list2.append(c.getvalue())
            return render(request,'HTML/train_details.html',{'s1':train_list2})

def get_train_list(request):
    if request.method=='POST':
        source_name=request.POST.get('source')
        dest_name=request.POST.get('Destination')
        conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
        cur=conn.cursor()
        myvar= cur.var(cx_Oracle.CURSOR)
        cur.callfunc('get_train_names',myvar,[source_name,dest_name])
        train_list1=myvar.getvalue().fetchall()
        train_list1=list(sum(train_list1, ()))
        final={}
        for i in train_list1:
            myvar3= cur.var(cx_Oracle.CURSOR)
            cur.callfunc('get_train_details',myvar3,[i])
            train_list2=myvar3.getvalue().fetchall()
            train_list2=list(sum(train_list2,()))
            myvar2= cur.var(cx_Oracle.CURSOR)
            s=train_list2[0]
            cur.callfunc('get_train_route',myvar2,[s])
            t=myvar2.getvalue().fetchall()
            c=cur.var(int)
            cur.callproc('seat_avail',[i,c])
            train_info_list=list(sum(t, ()))
            train_list2.append(train_info_list)
            train_list2.append(c.getvalue())
            final[i]=train_list2
        
        print(final)
        return render(request,'HTML/train_names.html',{'t_names':train_list1,'s':source_name,'d':dest_name,'details':final})
def send_email(request):
    conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
    cur=conn.cursor()
    c=cur.var(cx_Oracle.CURSOR)
    cur.callproc('b_type',['SECUNDERABAD - VISAKHAPATNAM AC DURONTO EXPRESS','AC',c])
    t=c.getvalue().fetchall()
    t1=t[0][0]
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    e_mail=request.POST.get('email')
    print(e_mail)
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    src=request.POST.get('source')
    dest=request.POST.get('destination')
    date=request.POST.get('date')
    n=random.randint(1000000000,9999999999)
    
    html_message = loader.render_to_string(
                                'HTML/mail_body.html',
                                {
                                    'fname' : fname,
                                    'lname' : lname,
                                    'gender': gender,
                                    'age' : age,
                                     's':src,
                                    'dest' : dest,
                                    'date':date,
                                    'seat':t1
                                    
                                }
                            )
    send_mail('BOOKING',None,settings.EMAIL_HOST_USER,[e_mail],fail_silently=True,html_message=html_message)
    messages.success(request,"Mails have been sent on your mail !")
    return redirect('Home')
from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# def get_train_info(request):
#     if request.method=='POST':
#         train_name=request.POST.get('term')
#         print(train_name)
#         conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
#         cur=conn.cursor()
#         myvar3= cur.var(cx_Oracle.CURSOR)
#         cur.callfunc('get_train_details',myvar3,[train_name])
#         train_list2=myvar3.getvalue().fetchall()
#         train_list2=list(sum(train_list1,()))
#         myvar2= cur.var(cx_Oracle.CURSOR)
#         s=train_list2[0]
#         cur.callfunc('get_train_route',myvar2,[s])
#         t=myvar2.getvalue().fetchall()
#         train_info_list=list(sum(t, ()))
#         train_list2.append(train_info_list)
#         print(train_list2)
#         return render(request,'HTML/train_names.html',{'t_names2':train_list1,'route':train_info_list})
