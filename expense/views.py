from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import CreateView
from django.core import serializers
from django.http import JsonResponse

def dashboard(request):
    
    qr = Expense.objects.all()

    return render(  request , 'dashboard/dashboard.html' , { 'data' : qr} )

def load_json_data(request):
    dataset = Expense.objects.all()
    data = serializers.serialize('json',dataset)
    return JsonResponse(data, safe=False)

class CreateExpense( CreateView ):
        model =  Expense
        form_class = ExpenseForm
        success_url = '/expense/dashboard'
        
