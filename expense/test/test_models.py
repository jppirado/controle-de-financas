from django.test import TestCase
from ..models import Expense 
from datetime import datetime


class TestExpense(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Expense.objects.create(name='Compra do mes',value=100.0,date=datetime.now() )

    def test_name_integridade(self):
        expense = Expense.objects.get(id=1)
        max_length  = expense._meta.get_field('name').max_length
        self.assertEquals(max_length,255) 
    
    def test_float_integridade(self):
        expense = Expense.objects.get(id=1)
        max_length  = expense._meta.get_field('value').max_length
        self.assertEquals(max_length,10) 
    
    def test__str__function(self):
        expense = Expense.objects.get(id=1)
        self.assertEquals(expense.name , 'Compra do mes')