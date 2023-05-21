from django.shortcuts import render


def dashboard(request):

    return render(  request , 'dashboard/dashboard.html' )

def create_expense(request): 

    return render(request, 'form/form_create.html')