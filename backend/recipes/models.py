from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIET_CHOICES = [
        ('all', 'General / Non-Specific'),
        ('keto', 'Keto Friendly'),
        ('vegan', 'Vegan / Vegetarian'),
        ('protein', 'High Protein'),
        ('gluten-free', 'Gluten-Free'),
    ]

    title = models.CharField(max_length=200, verbose_name="Recipe Title")
    slug = models.SlugField(unique=True, blank=True, null=True) 
    description = models.TextField(help_text="Briefly describe the dish")
    ingredients = models.TextField(help_text="Separate ingredients with a comma or new line")
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/%Y/%m/%d/', default='default_recipe.jpg')
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_recipes')
    
    diet_type = models.CharField(max_length=20, choices=DIET_CHOICES, default='all',null=True,blank=True)
    prep_time = models.PositiveIntegerField(default=30, help_text="Preparation time in minutes",null=True,blank=True)
    calories = models.PositiveIntegerField(default=500, help_text="Calories per serving",null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe') 
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.title}"