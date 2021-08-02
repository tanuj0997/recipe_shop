from collections import OrderedDict

from .models import CartItems, Cart
from recipes.models import Recipe
from .serializers import CartItemsSerializer, CartSerializer

from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CartItemsListView(APIView):
    """
    View to list all the contents inside a cart
    """
    serializer_class = CartItemsSerializer

    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"This cart does not exist"},
                            status.HTTP_404_NOT_FOUND)
        cart_items = CartItems.objects.filter(cart=cart)
        cart_data = OrderedDict()
        cart_items_serializer = self.serializer_class(cart_items, many=True)
        cart_serializer = CartSerializer(cart)
        cart_data.update({"items": cart_items_serializer.data})
        cart_data.update(cart_serializer.data)
        return Response(cart_data)


class AddItemToCartView(APIView):
    """
    View to add a recipe to a cart
    """
    serializer_class = CartItemsSerializer

    def post(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"This cart does not exist"},
                            status.HTTP_404_NOT_FOUND)
        recipe_id = request.data.get('recipe_id')
        if not recipe_id:
            return Response({"recipe_id is a required parameter"},
                            status.HTTP_400_BAD_REQUEST)
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            return Response({"This recipe does not exist"},
                            status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            # creating a new line item
            CartItems.objects.create(cart=cart, recipe=recipe)

            # updating price of cart
            cart.total_in_cents += recipe.price_in_cents
            cart.save()

        return Response({"Recipe added to cart"}, status.HTTP_200_OK)


class DeleteRecipeFromCartView(APIView):
    """
    View to delete a recipe from a cart
    """

    def delete(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(pk=kwargs.get('cart_id'))
        except Cart.DoesNotExist:
            return Response({"This cart does not exist"},
                            status.HTTP_404_NOT_FOUND)
        recipe_id = kwargs.get('recipe_id')
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            return Response({"This recipe does not exist"},
                            status.HTTP_404_NOT_FOUND)

        # finding instances of recipe in cart
        recipes_in_cart = CartItems.objects.filter(cart=cart, recipe=recipe)
        with transaction.atomic():
            if recipes_in_cart.exists():
                recipes_in_cart[0].delete()
            else:
                return Response({"This recipe does not exist in this cart"},
                                status.HTTP_404_NOT_FOUND)

            # updating price of cart
            cart.total_in_cents -= recipe.price_in_cents
            cart.save()
        return Response({"Recipe removed from cart"}, status.HTTP_200_OK)
