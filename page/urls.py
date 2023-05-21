from django.urls import path 
from .views import index_page , login

urlpatterns = [
    path('',  index_page , name='page.index'),
    path('login' , login, name='page.login' ),
]

