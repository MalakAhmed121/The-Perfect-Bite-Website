# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login  
from django.contrib.auth.models import User  
from django.http import JsonResponse 
from .forms import RegisterForm 
from .models import HealthyRecipe


# home page
def home(request):
    return render(request, "recipes/index.html")


def cover(request):
    return render(request, "recipes/cover.html")


def favorites(request):
    return render(request, "recipes/favorites.html")


def recipes_page(request):
    return render(request, "recipes/recipes.html")


def recipe_details(request):
    return render(request, "recipes/recipe-details.html")


def search_page(request):
    return render(request, "recipes/search.html")


def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get("next") or request.GET.get("next") or "home"
            return redirect(next_url)
        else:
            return render(
                request, "recipes/auth/login.html", {"error": "Invalid username or password"}
            )

    return render(request, "recipes/auth/login.html")


def signup_page(request):
   

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_type = request.POST.get('user_type')
            user = User.objects.create_user(username=username, password=password)

            if user_type == 'admin':
                user.is_staff = True
                user.is_superuser = True 
                user.save()

            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "recipes/auth/signup.html", {"form": form})


#  admin
def add_recipe(request):
    return render(request, "recipes/admin/add-recipe.html")


def admin_recipe(request):
    return render(request, "recipes/admin/admin-recipe.html")


def edit_recipe(request):
    return render(request, "recipes/admin/edit-recipe.html")


#  appetizers
def appetizers(request):
    return render(request, "recipes/appetizers/appetizers.html")


#  bakery
def bakery(request):
    return render(request, "recipes/bakery/bakery.html")


def bread(request):
    return render(request, "recipes/bakery/Bread .html")


def cinnamon(request):
    return render(request, "recipes/bakery/Cinnamon.html")


def cookies(request):
    return render(request, "recipes/bakery/cookies.html")


def croissants(request):
    return render(request, "recipes/bakery/Croissants .html")


def donuts(request):
    return render(request, "recipes/bakery/Donuts .html")


def macrons(request):
    return render(request, "recipes/bakery/macrons.html")


#  desserts
def dessert(request):
    return render(request, "recipes/desserts/dessert.html")


#  drinks
def drinks_page(request):
    return render(request, "recipes/drinks/drinks.html")


def coffee(request):
    return render(request, "recipes/drinks/coffee.html")


def hot_drinks(request):
    return render(request, "recipes/drinks/hot_drinks.html")


def juices(request):
    return render(request, "recipes/drinks/juices.html")


#  healthy



def healthy_food(request):

    all_healthy_recipes = HealthyRecipe.objects.all()

    return render(
        request, "recipes/healthy/Healthy Food.html", {"recipes": all_healthy_recipes}
    )




def get_recipe_details(request, recipe_id):
    try:
        recipe = HealthyRecipe.objects.get(id=recipe_id)

        data = {
            "title": recipe.title,
            "description": recipe.description,
            "ingredients": recipe.ingredients.split(","),
            "method": recipe.preparation_steps,
            "image_url": recipe.image.url,
            "calories": recipe.calories,
            "prep_time": recipe.prep_time,
        }
        return JsonResponse(data)
    except HealthyRecipe.DoesNotExist:
        return JsonResponse({"error": "recipe not found"}, status=404)


#  main_dish
def main_dish(request):
    return render(request, "recipes/main_dish/maindish.html")


def beef(request):
    return render(request, "recipes/main_dish/beef.html")


def chicken(request):
    return render(request, "recipes/main_dish/chicken.html")


def fastfood(request):
    return render(request, "recipes/main_dish/fastfood.html")


def pasta(request):
    return render(request, "recipes/main_dish/pasta.html")


def seafood(request):
    return render(request, "recipes/main_dish/seafood.html")


def vegetarian(request):
    return render(request, "recipes/main_dish/Vegetarian.html")
