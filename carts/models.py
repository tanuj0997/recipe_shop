from django.db import models
from products.models import Product
from recipes.models import Recipe


class Cart(models.Model):
    """
    Derived from the "carts" table in the assignment spec
    """
    total_in_cents = models.IntegerField()


class CartItems(models.Model):
    """
    Derived from the "cart_items" table in the assignment spec
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
