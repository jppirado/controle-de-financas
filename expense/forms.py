from django import forms
from .models import Expense

class ExpenseForm (forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name' , 'value','date']
    
    # def clean(self):
    #     self.instance.user = 
    #     print(dir(self))
    #     print(self)
       
    #     return self
    
   
        

