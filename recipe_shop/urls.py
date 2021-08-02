from django.contrib import admin
from django.urls import include, path
from recipes.views import ListRecipeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', ListRecipeView.as_view()),
]
