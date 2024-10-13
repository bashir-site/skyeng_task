from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    orders_last_month = models.IntegerField(default=0)
    orders_current_month = models.IntegerField(default=0)

    def calculate_orders(self):
        # Здесь должна быть логика для подсчета заказов
        # Для простоты, будем возвращать 0
        return 0

    def get_orders_last_month(self):
        # Логика подсчета заказов за прошлый месяц
        return self.orders_last_month

    def get_orders_current_month(self):
        # Логика подсчета заказов за текущий месяц
        return self.orders_current_month

    def __str__(self):
        return self.name
