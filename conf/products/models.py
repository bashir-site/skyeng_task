from datetime import datetime, timedelta

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
        last_month_start = datetime.now() - timedelta(days=30)
        return Order.objects.filter(
            product=self,
            order_date__gte=last_month_start
        ).count()

    def get_orders_current_month(self):
        current_month_start = datetime.now().replace(day=1)
        return Order.objects.filter(
            product=self,
            order_date__gte=current_month_start
        ).count()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Заказ товара {self.product.name} на дату: {self.order_date}"
