from django.shortcuts import redirect, render
from user.admin import CustomUserCreationForm

# Create your views here.

def login(request):
    return render(request , 'registration/login.html')

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            return redirect('user/')

        else:
            print('invalid registration details')
            
    return render(request, "registration/register.html",{"form": form})