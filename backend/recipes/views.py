# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import RegisterForm , RecipeForm 
from .models import HealthyRecipe , Recipe
from django.contrib.auth.decorators import login_required


# home page
@login_required(login_url="login")
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
                request,
                "recipes/auth/login.html",
                {"error": "Invalid username or password"},
            )

    return render(request, "recipes/auth/login.html")


def signup_page(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_type = request.POST.get("user_type")

            if not user_type or user_type not in ["user", "admin"]:
                return render(
                    request,
                    "recipes/auth/signup.html",
                    {"form": form, "error": "Please select user type (User or Admin)"},
                )

            user = User.objects.create_user(username=username, password=password)

            if user_type == "admin":
                user.is_staff = True
                user.is_superuser = True
                user.save()

            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "recipes/auth/signup.html", {"form": form})


#/////////////////admin////////////////////
def admin_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/admin/admin-recipe.html", {"recipes": recipes})

# //Add
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_recipe')
    else:
        form = RecipeForm()
    return render(request, "recipes/admin/add-recipe.html", {"form": form})

# //View
def view_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
      form = RecipeForm(request.POST,instance=recipe)
      if form.is_valid():
        form.save()
        return redirect('admin_recipe')
    return render(request, "recipes/admin/view-recipe.html", {'recipe': recipe})        

# //Edit
def edit_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('admin_recipe')
    else:
        form = RecipeForm(instance=recipe)    
    return render(request, 'recipes/admin/edit-recipe.html', {'form': form, 'recipe': recipe}) 

# //Delete
def delete_recipe(request, id):
   recipe = Recipe.objects.get(id=id)
   if request.method == 'POST':
         recipe.delete()
         return redirect('admin_recipe')
   return render(request, 'recipes/admin/delete-recipe.html', {'recipe': recipe}) 
    

#  appetizers
def appetizers(request):
    recipes = Recipe.objects.filter(course='appetizers')
    return render(request, "recipes/appetizers/appetizers.html", {"recipes": recipes})


#  bakery
def bakery(request):
    recipes = Recipe.objects.filter(course='bakery')
    return render(request, "recipes/bakery/bakery.html", {"recipes": recipes})


def bread(request):
    recipes = Recipe.objects.filter(course='bakery', name='Bread')
    return render(request, "recipes/bakery/Bread .html", {"recipes": recipes})


def cinnamon(request):
    recipes = Recipe.objects.filter(course='bakery', name='Cinnamon')
    return render(request, "recipes/bakery/Cinnamon.html", {"recipes": recipes})


def cookies(request):
    recipes = Recipe.objects.filter(course='bakery', name='Cookies')
    return render(request, "recipes/bakery/cookies.html", {"recipes": recipes})


def croissants(request):
    recipes = Recipe.objects.filter(course='bakery', name='Croissants')
    return render(request, "recipes/bakery/Croissants .html", {"recipes": recipes})


def donuts(request):
    recipes = Recipe.objects.filter(course='bakery', name='Donuts')
    return render(request, "recipes/bakery/Donuts .html", {"recipes": recipes})


def macrons(request):
    recipes = Recipe.objects.filter(course='bakery', name='Macrons')
    return render(request, "recipes/bakery/macrons.html", {"recipes": recipes})


#  desserts
def dessert(request):
    recipes = Recipe.objects.filter(course='desserts')
    return render(request, "recipes/desserts/dessert.html", {"recipes": recipes})


#  drinks
def drinks_page(request):
    recipes = Recipe.objects.filter(course='drinks')
    return render(request, "recipes/drinks/drinks.html", {"recipes": recipes})


def coffee(request):
    recipes = Recipe.objects.filter(course='drinks', name='Coffee')
    return render(request, "recipes/drinks/coffee.html", {"recipes": recipes})


def hot_drinks(request):
    recipes = Recipe.objects.filter(course='drinks', name='Hot Drinks')
    return render(request, "recipes/drinks/hot_drinks.html", {"recipes": recipes})


def juices(request):
    recipes = Recipe.objects.filter(course='drinks', name='Juices')
    return render(request, "recipes/drinks/juices.html", {"recipes": recipes})


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
    recipes = Recipe.objects.filter(course='main_dish')
    return render(request, "recipes/main_dish/maindish.html", {"recipes": recipes})


def beef(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Beef')
    return render(request, "recipes/main_dish/beef.html", {"recipes": recipes})


def chicken(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Chicken')
    return render(request, "recipes/main_dish/chicken.html", {"recipes": recipes})


def fastfood(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Fast Food')
    return render(request, "recipes/main_dish/fastfood.html", {"recipes": recipes})


def pasta(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Pasta')
    return render(request, "recipes/main_dish/pasta.html", {"recipes": recipes})


def seafood(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Seafood')
    return render(request, "recipes/main_dish/seafood.html", {"recipes": recipes})


def vegetarian(request):
    recipes = Recipe.objects.filter(course='main_dish', name='Vegetarian')
    return render(request, "recipes/main_dish/Vegetarian.html", {"recipes": recipes})
