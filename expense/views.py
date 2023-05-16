from django.shortcuts import render
from .models import Expense

def index( request ):

    if not request.method == 'POST':
        pass


    return render( request ,'index_list.html')