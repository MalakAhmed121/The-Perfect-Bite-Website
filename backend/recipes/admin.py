from django.contrib import admin
from .models import Recipe, Category, Favorite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_recipes_count') 
    search_fields = ('name',)

    def get_recipes_count(self, obj):
        return obj.recipes.count()
    get_recipes_count.short_description = 'Number of Recipes'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'diet_type', 'author', 'prep_time', 'calories', 'created_at')
    list_filter = ('category', 'diet_type', 'author', 'created_at')
    search_fields = ('title', 'ingredients', 'description')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'author', 'image')
        }),
        ('Healthy Details', {
            'description': 'Specific info for the Healthy Food page',
            'fields': ('diet_type', 'prep_time', 'calories'),
        }),
        ('Content Details', {
            'fields': ('description', 'ingredients', 'instructions'),
            'classes': ('collapse',), 
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'added_at')
    list_filter = ('user', 'added_at')
    