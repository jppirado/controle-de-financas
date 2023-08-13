
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/' , include('expense.urls')),
    path('user' , include('user.urls')), 
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('page.urls') ),
]

