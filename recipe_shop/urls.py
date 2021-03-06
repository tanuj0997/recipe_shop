from django.contrib import admin
from django.urls import include, path
from recipes.views import ListRecipeView
from carts.views import CartItemsListView, AddItemToCartView, DeleteRecipeFromCartView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', ListRecipeView.as_view(), name='recipe-list'),
    path('carts/<int:pk>/', CartItemsListView.as_view(), name='cart-details'),
    path('carts/<int:pk>/add_recipe/',
         AddItemToCartView.as_view(), name='add-recipe'),
    path('carts/<int:cart_id>/recipes/<int:recipe_id>/',
         DeleteRecipeFromCartView.as_view(), name='delete-recipe')

]
