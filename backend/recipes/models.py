from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('healthy', 'Healthy'),
        ('maindish', 'Main Dish'),
        ('bakery', 'Bakery'),
        ('dessert', 'Dessert'),
        ('drinks', 'Drinks'),
        ('appetizers', 'Appetizers'),
    ]

    name = models.CharField(max_length=200)
    course = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='recipes_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.course})"


class HealthyRecipe(models.Model):
    DIET_CHOICES = [
        ('keto', 'Keto Friendly'),
        ('vegan', 'Vegan / Vegetarian'),
        ('protein', 'High Protein'),
        ('gluten-free', 'Gluten-Free'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    calories = models.IntegerField()
    prep_time = models.IntegerField()
    diet_type = models.CharField(max_length=20, choices=DIET_CHOICES)
    image = models.ImageField(upload_to='healthy_photos/')

    def __str__(self):
        return self.title

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"