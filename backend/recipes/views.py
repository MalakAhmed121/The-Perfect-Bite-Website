from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import RegisterForm, RecipeForm 
from .models import Recipe, Category, Favorite
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

# --- الصفحات الأساسية ---

@login_required(login_url="login")
def home(request):
    latest_recipes = Recipe.objects.select_related('category', 'author').all()[:6]
    return render(request, "recipes/index.html", {"recipes": latest_recipes})

def cover(request):
    return render(request, "recipes/cover.html")

@login_required(login_url="login")
def favorites(request):
    user_favorites = Favorite.objects.filter(user=request.user).select_related('recipe')
    return render(request, "recipes/favorites.html", {"favorites": user_favorites})

def recipes_page(request):
    all_recipes = Recipe.objects.all()
    return render(request, "recipes/recipes.html", {"recipes": all_recipes})

def recipe_details(request, slug): 
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "recipes/recipe-details.html", {'recipe': recipe})

def search_page(request):
    return render(request, "recipes/search.html")

def ajax_search(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'title')

    if search_type == 'ingredients':
        recipes = Recipe.objects.filter(
            ingredients__icontains=query
        )
    else:
        recipes = Recipe.objects.filter(
            title__icontains=query
        )

    data = [
        {
            "id": r.id,
            "slug": r.slug,
            "title": r.title,
            "description": r.description,
            "image": r.image.url if r.image else ""
        }
        for r in recipes
    ]

    return JsonResponse({"results": data})

# --- نظام التصنيفات (الحل لمشكلة صفحة Healthy) ---

def category_detail(request, category_name):
    # تحويل النص لصيغة موحدة للبحث
    category_slug = category_name.lower().replace("-", " ").strip()
    
    # 1. التحقق إذا كان المطلوب هو صفحة Healthy
    if category_slug == 'healthy':
        recipes = Recipe.objects.filter(diet_type__in=['keto', 'vegan', 'protein', 'gluten-free'])
        return render(request, "recipes/healthy/Healthy Food.html", {
            "recipes": recipes,
            "category": "Healthy Food"
        })
    
    # 2. التعامل مع باقي التصنيفات ديناميكياً
    category_obj = get_object_or_404(Category, name__iexact=category_slug)
    recipes = Recipe.objects.filter(category=category_obj)
    
    # Smart Template Selection
    category_slug = category_slug.lower()
    clean_name = category_slug.replace(" ", "_").replace("-", "_")
    simple_name = category_slug.replace(" ", "").replace("-", "")
    
    # Hardcoded hub mapping for reliability
    hub_templates = {
        'bakery': 'recipes/bakery/bakery.html',
        'main dish': 'recipes/main_dish/maindish.html',
        'healthy': 'recipes/healthy/Healthy Food.html',
        'drinks': 'recipes/drinks/drinks.html',
        'dessert': 'recipes/desserts/dessert.html',
        'appetizers': 'recipes/appetizers/appetizers.html',
    }
    
    template_name = hub_templates.get(category_slug)
    
    if not template_name:
        # List of possible template paths for sub-categories
        possible_templates = [
            f"recipes/{clean_name}/{clean_name}.html",
            f"recipes/{clean_name}/{simple_name}.html",
            f"recipes/main_dish/{clean_name}.html",
            f"recipes/main_dish/{simple_name}.html",
            f"recipes/bakery/{clean_name}.html",
            f"recipes/bakery/{simple_name}.html",
            f"recipes/{clean_name}s/{clean_name}.html",
            f"recipes/drinks/{clean_name}.html",
            f"recipes/desserts/{clean_name}.html",
            f"recipes/bakery/macrons.html" if clean_name == "macarons" else None,
        ]
        possible_templates = [t for t in possible_templates if t]
        
        template_name = None
        for t in possible_templates:
            try:
                get_template(t)
                template_name = t
                break
            except TemplateDoesNotExist:
                continue
        
        # If still no template found, default to a sensible one
        if not template_name:
            template_name = "recipes/recipes.html"

    return render(request, template_name, {
        "recipes": recipes, 
        "category": category_obj.name,
        "category_obj": category_obj
    })


def signup_page(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_type = request.POST.get('user_type')
            
            
            if not user_type or user_type not in ['user', 'admin']:
                return render(request, 'recipes/auth/signup.html', {
                    'form': form,
                    'error': 'Please select user type (User or Admin)'
                })
            
            user = User.objects.create_user(username=username, password=password)
            
            if user_type == 'admin':
                user.is_staff = True
                user.is_superuser = True
                user.save()
            
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'recipes/auth/signup.html', {'form': form})

def login_page(request):
  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            return render(request, 'recipes/auth/login.html', {'error': 'Invalid username or password'})

    return render(request, 'recipes/auth/login.html')

def logout_user(request):
    logout(request)
    return redirect("login")

# --- لوحة تحكم الإدارة (Admin Portal) ---

@login_required(login_url="login")
def admin_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/admin/admin-recipe.html", {"recipes": recipes})

@login_required(login_url="login")
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('admin_recipe')
    else:
        form = RecipeForm()
    return render(request, "recipes/admin/add-recipe.html", {"form": form})




@login_required(login_url="login")
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('admin_recipe')
    else:
        form = RecipeForm(instance=recipe)    
    return render(request, 'recipes/admin/edit-recipe.html', {'form': form, 'recipe': recipe}) 

@login_required(login_url="login")
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('admin_recipe')
    return render(request, 'recipes/admin/delete-recipe.html', {'recipe': recipe})

@login_required(login_url="login")
def toggle_favorite(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
        
        if not created:
            favorite.delete()
            is_favorite = False
        else:
            is_favorite = True
            
        return JsonResponse({"status": "success", "is_favorite": is_favorite})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)