from rest_framework.serializers import ModelSerializer
from .models import CartItems, Cart

from products.serializers import ProductSerializer
from recipes.serializers import RecipeSerializer


class CartItemsSerializer(ModelSerializer):

    # preserving the existing field, not covered in current scope
    product = ProductSerializer()
    recipe = RecipeSerializer()

    class Meta:
        model = CartItems
        fields = ['product', 'recipe']
        depth = 1


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ['total_in_cents']
