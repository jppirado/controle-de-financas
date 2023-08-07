from typing import Any, Dict
from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import CreateView
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Sum
from django.views.generic import ListView

def dashboard(request):
    soma = Expense.objects.filter(user=request.user).aggregate(total_sum=Sum('value'))
    return render(  request , 'dashboard/dashboard.html' , {'total':soma } )

def load_json_data(request):
    dataset = Expense.objects.filter(user=request.user)
    data = serializers.serialize('json',dataset)
    return JsonResponse(data, safe=False)

class CreateExpense( CreateView ):
    model =  Expense
    form_class = ExpenseForm
    success_url = '/expense/dashboard'
        
    def get_context_data(self, **kwargs):
        data = super(CreateExpense, self).get_context_data(**kwargs)
        if self.request.POST:
            data['form'] = ExpenseForm(self.request.POST)
        else:
            data['form'] = ExpenseForm()
        return data 
        
    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user       
            form.save()
        return super(CreateExpense, self).form_valid(form)
    
class ListAllExpenses(ListView):
    model = Expense
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context  = super().get_context_data(**kwargs)
        context['object_list'] = Expense.objects.filter(user=self.request.user)
        return context
