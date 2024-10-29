from django.db import models
from django.contrib.auth.models import User
import uuid



class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField(max_length=254)
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


# Modelo Product
class Product(models.Model):
    product_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(max_length=200,null=True, blank=True)
    #imagen = models.ImageField(upload_to='imagenes/')
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # Agregaré a lo solicitado en actividad
    delivery = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

# Modelo para el Cliente
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Modelo para Orden
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

# Modelo para Orden-Producto
class OrderItem(models.Model):
    product_uuid = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_uuid.name} x {self.quantity}"

# Modelo para Envío
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
