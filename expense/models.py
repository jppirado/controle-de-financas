from django.db import models
from datetime import datetime

# Create your models here.

class Expense( models.Model ):

    name = models.CharField("Nome da Compra" , max_length=255)
    value = models.FloatField()
    date = models.DateField("Data da compra" , default=datetime.now())
    
    
    def __str__(self):
        return self.name
