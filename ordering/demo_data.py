from ordering.models import company, profile, Product, order
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import random

def create_demo_data():
    # Create companies
    company1 = company.objects.create(name="TechCorp")
    company2 = company.objects.create(name="FoodInc")

    # Create users
    user1 = profile.objects.create(user="alice", password=make_password("pass123"), role="operator", company=company1)
    user2 = profile.objects.create(user="bob", password=make_password("pass123"), role="viewer", company=company2)

    # Create products
    for i in range(5):
        Product.objects.create(
            name=f"Laptop Model {i}",
            company=company1,
            price=random.randint(5000, 15000),
            stock=random.randint(10, 50)
        )

    for i in range(5):
        Product.objects.create(
            name=f"Snack Pack {i}",
            company=company2,
            price=random.randint(10, 50),
            stock=random.randint(100, 300)
        )

    # Create orders
    products = Product.objects.all()
    for i in range(10):
        order.objects.create(
            name=f"order {i}",
            product=random.choice(products),
            quantity=random.randint(1, 5),
            created_by=random.choice([user1, user2]),
        )

    print("✅ Demo data created successfully!")
