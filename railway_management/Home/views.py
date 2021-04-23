from django.shortcuts import render,redirect,HttpResponse,Http404,HttpResponsePermanentRedirect

def index(request):

    return render(request,'HTML/index.html')

# Create your views here.
