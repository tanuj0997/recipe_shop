from django.db import models
from products.models import Product


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    price_in_cents = models.IntegerField()


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
