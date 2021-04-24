from django.shortcuts import render,redirect,HttpResponse,Http404,HttpResponsePermanentRedirect

def index(request):
    return render(request,'HTML/index.html')

def get_train_details(request):
    return render(request,'HTML/get_train_details.html')

def book_seat(request):
    return render(request,'HTML/booking.html')