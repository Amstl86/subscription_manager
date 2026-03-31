from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Подписки"""
    
    class Meta:
        model = Subscription
        fields = [
            'id', 'name', 'price', 'currency', 'billing_cycle',
            'start_date', 'next_payment_date', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']