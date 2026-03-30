from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Subscription(models.Model):
    """Модель подписки пользователя"""
    
    name = models.CharField(max_length=100, verbose_name="Название сервиса")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    currency = models.CharField(max_length=3, default='USD', verbose_name="Валюта")
    billing_cycle = models.CharField(
        max_length=20,
        choices=[
            ('monthly', 'Ежемесячно'),
            ('yearly', 'Ежегодно'),
            ('weekly', 'Еженедельно'),
        ],
        default='monthly',
        verbose_name="Период оплаты"
    )
    start_date = models.DateField(verbose_name="Дата начала")
    next_payment_date = models.DateField(verbose_name="Дата следующего платежа")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['next_payment_date']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}"

    def calculate_next_payment(self):
        """Расчет даты следующего платежа"""
        
        
        if self.billing_cycle == 'monthly':
            return self.next_payment_date + relativedelta(months=1)
        elif self.billing_cycle == 'yearly':
            return self.next_payment_date + relativedelta(years=1)
        elif self.billing_cycle == 'weekly':
            return self.next_payment_date + relativedelta(weeks=1)
        
        return self.next_payment_date