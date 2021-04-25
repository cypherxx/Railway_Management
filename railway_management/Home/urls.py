from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('train_details',views.train_details,name='gtd'),
    path('book_details',views.book_seat,name='book'),
    path('train_list',views.get_train_list,name='train_list'),
    path('train_detail',views.get_train_info,name='train_detail')
]
