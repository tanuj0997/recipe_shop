from django.urls import reverse

from rest_framework.test import APITestCase


from recipes.models import Recipe


class RecipeTests(APITestCase):

    fixtures = [
        'recipes/fixtures/recipe_fixtures.json',
    ]

    def test_list_recipes(self):
        """
        This test tests whether the list of recipes are obtained correctly
        """

        # testing if the API call succeeds
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # verifying data
        self.assertEqual(len(response.data), 2)
