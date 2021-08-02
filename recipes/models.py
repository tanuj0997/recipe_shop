from django.db import models
from products.models import Product


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    price_in_cents = models.IntegerField()


class RecipeProduct(models.Model):
    """
    This model is used to store the ingredients (i.e. associated products)
    of a recipe. According to requirement spec, although this model fulfils
    the requirement of being able to store the ingredients of the recipe, it
    will not be in active use.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
