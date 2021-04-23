from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('train_details',views.get_train_details,name='gtd'),
    path('book_details',views.book_seat,name='book')
]
