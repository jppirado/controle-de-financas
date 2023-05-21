from django.urls import path
from .views import dashboard,create_expense

urlpatterns = [
    path('/dashboard' , dashboard, name="expense.dashboard"),
    path('/dashboard/create' , create_expense, name="expense.create"),
]
