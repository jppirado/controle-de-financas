from django.test import TestCase
from ..models import Expense
from datetime import datetime

class TestDashBoard(TestCase):
    @classmethod
    def setUpTestData(cls):
        for expense in range(100):
            Expense.objects.create(
                name=f'Christian {expense}',
                value=expense,
                date=datetime.now()
        )
        
    def test_url_view_exists(self):
        response = self.client.get('/expense/dashboard')
        self.assertEqual(response.status_code, 200)
        
        