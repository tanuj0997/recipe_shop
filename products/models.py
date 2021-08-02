from django.db import models


class Product(models.Model):
    """
    Derived from the "products" table in the assignment spec
    """
    name = models.CharField(max_length=200)
    price_in_cents = models.IntegerField()
