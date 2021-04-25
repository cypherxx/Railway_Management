from django.shortcuts import render,redirect,HttpResponse,Http404,HttpResponsePermanentRedirect
import cx_Oracle
from django.db import connection
from .models import TrainVkp1,BogieVkp1,BookingsVkp4,StationVkp1,RouteStationVkp1,RouteVkp1,SeatVkp1

def index(request):
    return render(request,'HTML/index.html')

def train_details(request):
    return render(request,'HTML/get_train_details.html')

def book_seat(request):
    return render(request,'HTML/booking.html')

def get_train_list(request):
    if request.method=='POST':
        source_name=request.POST.get('source')
        dest_name=request.POST.get('Destination')
        conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
        cur=conn.cursor()
        myvar= cur.var(cx_Oracle.CURSOR)
        cur.callfunc('get_train_names',myvar,[source_name,dest_name])
        train_list1=myvar.getvalue().fetchall()
        print(train_list1)
        return render(request,'HTML/train_names.html',{'t_names':train_list1,'s':source_name,'d':dest_name})

def get_train_info(request):
    if request.method=='POST':
        train_name=request.POST.get('term')
        print(train_name,'Vaishnavi')
        conn=cx_Oracle.connect('qwerty','qwerty','localhost/orcl',encoding = 'UTF-8')
        cur=conn.cursor()
        myvar= cur.var(cx_Oracle.CURSOR)
        cur.callfunc('get_train_details',myvar,[train_name])
        train_list1=myvar.getvalue().fetchall()
        train_list1=list(sum(train_list1,()))
        myvar2= cur.var(cx_Oracle.CURSOR)
        s=train_list1[0]
        cur.callfunc('get_train_route',myvar2,[s])
        t=myvar2.getvalue().fetchall()
        train_info_list=list(sum(t, ()))
        train_list1.append(train_info_list)
        print(train_list1)
        return render(request,'HTML/train_names.html',{'t_names2':train_list1,'route':train_info_list})



