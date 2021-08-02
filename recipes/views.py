from rest_framework.generics import ListAPIView
from .serializers import RecipeSerializer
from .models import Recipe


class ListRecipeView(ListAPIView):
    """
    View to list all the recipes
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
