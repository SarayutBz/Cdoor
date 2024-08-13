# myapp/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import User
import json

class UserCreationTest(TestCase):
    def test_create_user(self):
        url = reverse('create_user')
        data = {
            'username': 'testuser',
            'password_hash': 'hashed_password',
            'email': 'testuser@example.com'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        
        # ตรวจสอบว่า response status code เป็น 201 (Created)
        self.assertEqual(response.status_code, 201)
        
        # ตรวจสอบว่าข้อมูลถูกสร้างในฐานข้อมูล
        self.assertTrue(User.objects.filter(username='testuser').exists())
        
        # ตรวจสอบเนื้อหาใน response
        self.assertEqual(response.json()['username'], 'testuser')
        self.assertEqual(response.json()['email'], 'testuser@example.com')
