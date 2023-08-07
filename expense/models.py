from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Expense( models.Model ):
    name = models.CharField("Nome da Compra" , max_length=255)
    value = models.FloatField()
    date = models.DateField("Data da compra" , default=datetime.now())
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    
    def __str__(self):
        return self.name
