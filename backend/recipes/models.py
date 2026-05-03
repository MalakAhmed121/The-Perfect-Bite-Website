from django.db import models



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
