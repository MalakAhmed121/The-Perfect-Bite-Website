

# Create your views here.

from django.shortcuts import render


# home page
def home(request):
    return render(request, 'recipes/index.html')

def cover(request):
    return render(request, 'recipes/cover.html')

def favorites(request):
    return render(request, 'recipes/favorites.html')

def recipes_page(request):
    return render(request, 'recipes/recipes.html')

def recipe_details(request):
    return render(request, 'recipes/recipe-details.html')

def search_page(request):
    return render(request, 'recipes/search.html')

def login_page(request):
    return render(request, 'recipes/auth/login.html')

def signup_page(request):
    return render(request, 'recipes/auth/signup.html')

#  admin
def add_recipe(request):
    return render(request, 'recipes/admin/add-recipe.html')

def admin_recipe(request):
    return render(request, 'recipes/admin/admin-recipe.html')

def edit_recipe(request):
    return render(request, 'recipes/admin/edit-recipe.html')

#  appetizers
def appetizers(request):
    return render(request, 'recipes/appetizers/appetizers.html')

#  bakery
def bakery(request):
    return render(request, 'recipes/bakery/bakery.html')

def bread(request):
    return render(request, 'recipes/bakery/Bread .html')

def cinnamon(request):
    return render(request, 'recipes/bakery/Cinnamon.html')

def cookies(request):
    return render(request, 'recipes/bakery/cookies.html')

def croissants(request):
    return render(request, 'recipes/bakery/Croissants .html')

def donuts(request):
    return render(request, 'recipes/bakery/Donuts .html')

def macrons(request):
    return render(request, 'recipes/bakery/macrons.html')

#  desserts
def dessert(request):
    return render(request, 'recipes/desserts/dessert.html')

#  drinks
def drinks_page(request):
    return render(request, 'recipes/drinks/drinks.html')

def coffee(request):
    return render(request, 'recipes/drinks/coffee.html')

def hot_drinks(request):
    return render(request, 'recipes/drinks/hot_drinks.html')

def juices(request):
    return render(request, 'recipes/drinks/juices.html')

#  healthy
from django.shortcuts import render
from .models import HealthyRecipe 

def healthy_food(request):
    
    all_healthy_recipes = HealthyRecipe.objects.all() 
    

    return render(request, 'recipes/healthy/Healthy Food.html', {'recipes': all_healthy_recipes})
from django.http import JsonResponse

def get_recipe_details(request, recipe_id):
    try:
        
        recipe = HealthyRecipe.objects.get(id=recipe_id)
        
        
        data = {
            'title': recipe.title,
            'description': recipe.description,
            'ingredients': recipe.ingredients.split(','), 
            'method': recipe.preparation_steps,
            'image_url': recipe.image.url,
            'calories': recipe.calories,
            'prep_time': recipe.prep_time,
        }
        return JsonResponse(data)
    except HealthyRecipe.DoesNotExist:
        return JsonResponse({'error': 'الوجبة غير موجودة'}, status=404)
#  main_dish
def main_dish(request):
    return render(request, 'recipes/main_dish/maindish.html')

def beef(request):
    return render(request, 'recipes/main_dish/beef.html')

def chicken(request):
    return render(request, 'recipes/main_dish/chicken.html')

def fastfood(request):
    return render(request, 'recipes/main_dish/fastfood.html')

def pasta(request):
    return render(request, 'recipes/main_dish/pasta.html')

def seafood(request):
    return render(request, 'recipes/main_dish/seafood.html')

def vegetarian(request):
    return render(request, 'recipes/main_dish/Vegetarian.html')

