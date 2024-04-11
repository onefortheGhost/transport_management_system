from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Vehicle

# Create your tests here.

User = get_user_model()

class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Test@123')

    def tearDown(self):
        self.user.delete()
    
    def test_login_with_valid_credentials(self):
        url = reverse('login')
        response = self.client.post(url,{'username': 'testuser', 'password':'Test@123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/')

    def test_login_with_invalid_credentials(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'testuser', 'password':'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password.')

class VehicleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Test@123')
        self.client.login(username = 'testuser', password = 'Test@123')
        self.vehicle = Vehicle.objects.create(
            make = 'Toyota',
            model = 'Camry',
            year = 2022
        )
    
    def test_vehicle_list(self):
        url = reverse('vehicle_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')
        self.assertContains(response, 'Camry')

    def test_vehicle_detail(self):
        url = reverse('vehicle_detail', args=[self.vehicle.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')
        self.assertContains(response, 'Camry')

    def test_vehicle_create(self):
        url = reverse('vehicle_create')
        data = {
            'make': 'Honda',
            'model': 'Civic',
            'year': 2023,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Vehicle.objects.count(), 2)
    
    def test_vehicle_update(self):
        url = reverse('vehicle_update', args=[self.vehicle.pk])
        data = {
            'make': 'Toyota',
            'model': 'Corolla',
            'year': 2022,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.model, 'Corolla')

    def test_vehicle_delete(self):
        url = reverse('vehicle_delete', args=[self.vehicle.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Vehicle.objects.count(), 0)