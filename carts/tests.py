from rest_framework.test import APITestCase

from .models import Cart
from recipes.models import Recipe


class CartTests(APITestCase):

    fixtures = [
        'products/fixtures/product_fixtures.json',
        'recipes/fixtures/recipe_fixtures.json',
    ]

    def setUp(self):
        self.cart = Cart.objects.create()

    def test_add_recipe(self):
        """
        This test tests whether a recipe can be added to the cart and
        if the total cart value is updated correctly
        """
        # obtaining recipe object to read its price later
        recipe = Recipe.objects.get(pk=1)
        original_cart_total = self.cart.total_in_cents

        # testing if the API call succeeds
        data = {'recipe_id': recipe.pk}
        url = f'/carts/{self.cart.pk}/add_recipe/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        # verifying the result
        verification_url = f'/carts/{self.cart.pk}/'
        verification_response = self.client.get(verification_url)
        self.assertEqual(response.status_code, 200)
        price_difference = verification_response.data.get(
            'total_in_cents') - original_cart_total
        self.assertEqual(price_difference, recipe.price_in_cents)
