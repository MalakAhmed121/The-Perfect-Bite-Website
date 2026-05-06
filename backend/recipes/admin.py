from django.contrib import admin
from .models import HealthyRecipe, Recipe, Favorite, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(HealthyRecipe)
class HealthyRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'diet_type', 'calories', 'prep_time')
    list_filter = ('diet_type',)
    search_fields = ('title',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    list_filter = ('user',)