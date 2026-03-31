import pytest
from rest_framework.test import APITestCase
from .models import Subscription
from datetime import date


class SubscriptionModelTest(APITestCase):
    """Тесты для модели подписки"""
    
    def test_create_subscription(self):
        """Проверка создания подписки"""
        sub = Subscription.objects.create(
            name="Netflix",
            price=15.99,
            currency="USD",
            billing_cycle="monthly",
            start_date=date(2026, 1, 1),
            next_payment_date=date(2026, 2, 1)
        )
        self.assertEqual(str(sub), "Netflix - 15.99 USD")
        self.assertTrue(sub.is_active)


class SubscriptionAPITest(APITestCase):
    """Тесты для API"""
    
    def test_list_subscriptions(self):
        """Проверка получения списка подписок"""
        response = self.client.get('/api/subscriptions/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_subscription_via_api(self):
        """Проверка создания подписки через API"""
        data = {
            "name": "Spotify",
            "price": "9.99",
            "currency": "USD",
            "billing_cycle": "monthly",
            "start_date": "2026-01-01",
            "next_payment_date": "2026-02-01",
            "is_active": True
        }
        response = self.client.post('/api/subscriptions/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subscription.objects.count(), 1)