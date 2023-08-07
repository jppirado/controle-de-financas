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
        print(self) 
        print(form)
        print(dir(form))
        if form.is_valid():
            form.instance.user = self.request.user       
            form.save()
        return super(CreateExpense, self).form_valid(form)