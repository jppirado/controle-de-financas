from django.urls import path
from .views import dashboard,create_expense
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('/dashboard' , login_required(dashboard), name="expense.dashboard"),
    path('/dashboard/create' , login_required(create_expense), name="expense.create"),
]
