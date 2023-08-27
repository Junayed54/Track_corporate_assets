from django.test import TestCase

# Create your tests here.
# app/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company

class CompanyAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(name="Test Company", address="Test Address")

    def test_get_company_list(self):
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_company_detail(self):
        response = self.client.get(f'/api/companies/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)
