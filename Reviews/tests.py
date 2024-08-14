from django.test import TestCase, Client
from django.urls import reverse
from .models import Review, Property
from django.contrib.auth.models import User
import json

class ReviewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.property = Property.objects.create(name='Test Property', location='Test Location')
        self.review = Review.objects.create(property=self.property, user=self.user, rating=5, comment='Great place!')

    def test_get_reviews(self):
        response = self.client.get(reverse('review-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Great place!')

    def test_get_review_detail(self):
        response = self.client.get(reverse('review-detail', args=[self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Great place!')

    def test_create_review(self):
        self.client.login(username='testuser', password='testpass')  # Simulate login
        data = {
            "property": self.property.id,
            "rating": 4,
            "comment": "Good place!"
        }
        response = self.client.post(reverse('create-review'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Review.objects.count(), 2)
        self.assertEqual(Review.objects.last().comment, 'Good place!')

    def test_create_review_missing_field(self):
        self.client.login(username='testuser', password='testpass')  # Simulate login
        data = {
            "property": self.property.id,
            "rating": 4,
            # Missing comment field
        }
        response = self.client.post(reverse('create-review'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing field', response.json()['error'])
