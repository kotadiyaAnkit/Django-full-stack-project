from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_offer = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    person_name = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=20, default="")
    pincode = models.CharField(max_length=10, default="")
    delivery_address = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, choices=[('UPI', 'UPI'), ('Offline', 'Offline Payment'), ('Online', 'Online Payment')], default='Offline')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
# Create your models here.

class PaymentSettings(models.Model):
    qr_code_image = models.ImageField(upload_to='payment_qr/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment Setting'
        verbose_name_plural = 'Payment Settings'

    def __str__(self):
        return "Payment Settings"