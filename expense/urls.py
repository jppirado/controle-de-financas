from django.urls import path
from .views import dashboard, CreateExpense, load_json_data
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('dashboard' , login_required(dashboard), name="expense.dashboard"),
    path('data', load_json_data, name='pivot_data'),
    path('dashboard/create' , login_required(CreateExpense.as_view() ), name="expense.create"),
]
