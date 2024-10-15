import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product, Category, Order
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Create 200 products'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')

        categories = ['Электроника', 'Одежда', 'Продукты', 'Книги', 'Игрушки']
        for cat in categories:
            Category.objects.get_or_create(name=cat)

        all_categories = Category.objects.all()

        start_of_current_month = datetime.now().replace(day=1)
        start_of_previous_month = (
            start_of_current_month - timedelta(days=1)
        ).replace(day=1)

        for _ in range(5):
            name = ' '.join(fake.words(nb=random.randint(2, 4))).title()
            category = random.choice(all_categories)
            status = random.choice(['active', 'inactive'])
            price = round(random.uniform(10.0, 1000.0), 2)
            orders_last_month = random.randint(0, 100)
            orders_current_month = random.randint(0, 100)

            product = Product.objects.create(
                name=name,
                category=category,
                status=status,
                price=price,
                orders_last_month=orders_last_month,
                orders_current_month=orders_current_month,
            )

            number_of_orders = random.randint(1, 60)
            for _ in range(number_of_orders):
                order_date = fake.date_time_between(
                    start_date=start_of_previous_month,
                    end_date=start_of_current_month
                )
                Order.objects.create(
                    product=product,
                    order_date=order_date
                )

        self.stdout.write(self.style.SUCCESS('OK'))
