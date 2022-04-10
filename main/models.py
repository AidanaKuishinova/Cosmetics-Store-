from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=60)

    def __str__(self) :
        return self.title+" "+self.url

class Product(models.Model):
    id=models.UUIDField(unique=True, primary_key=True)
    title = models.CharField(max_length=60, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name="Файл")
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    problems = models.TextField(blank=True, null=True)
    type_of_skin = models.TextField(blank=True, null=True)

    def __str__(self) :
        return self.title


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.IntegerField()
    products=models.ManyToManyField(Product,through='ProductItem')

    def __str__(self):
        return self.user.username

class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
