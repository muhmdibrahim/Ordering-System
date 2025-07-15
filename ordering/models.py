from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    roles = [
        ('operator', 'Operator'),
        ('viewer', 'Viewer')
    ]
    role = models.CharField(max_length=10, choices=roles, default='viewer')
    def __str__(self):
        return f"{self.user.username} - {self.role} at {self.company.name}"

class Product(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
class order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    Product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)