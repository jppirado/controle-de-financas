from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import CreateView

def dashboard(request):
    
    qr = Expense.objects.all()
    

    return render(  request , 'dashboard/dashboard.html' , { 'data' : qr} )

class CreateExpense( CreateView ):
        model =  Expense
        form_class = ExpenseForm
        success_url = '/expense/dashboard'