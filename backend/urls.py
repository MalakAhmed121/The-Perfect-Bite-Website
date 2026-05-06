from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # home pages
    path("", views.home, name="home"),
    path("cover/", views.cover, name="cover"),
    path("favorites/", views.favorites, name="favorites"),
    path("recipes/", views.recipes_page, name="recipes"),
    path("recipe-details/", views.recipe_details, name="recipe-details"),
    path("search/", views.search_page, name="search"),
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    # Admin
    path("add-recipe/", views.add_recipe, name="add_recipe"),
    path("admin_recipe/", views.admin_recipe, name="admin_recipe"),
    path("edit-recipe/", views.edit_recipe, name="edit_recipe"),
    # Appetizers
    path("appetizers/", views.appetizers, name="appetizers"),
    # Bakery
    path("bakery/", views.bakery, name="bakery"),
    path("bread/", views.bread, name="bread"),
    path("cinnamon/", views.cinnamon, name="cinnamon"),
    path("cookies/", views.cookies, name="cookies"),
    path("croissants/", views.croissants, name="croissants"),
    path("donuts/", views.donuts, name="donuts"),
    path("macrons/", views.macrons, name="macrons"),
    # Desserts
    path("dessert/", views.dessert, name="dessert"),
    # Drinks
    path("drinks/", views.drinks_page, name="drinks"),
    path("coffee/", views.coffee, name="coffee"),
    path("hot_drinks/", views.hot_drinks, name="hot_drinks"),
    path("juices/", views.juices, name="juices"),
    # Healthy
    path("healthy/", views.healthy_food, name="healthy"),
    path(
        "recipe-api/<int:recipe_id>/",
        views.get_recipe_details,
        name="get_recipe_details",
    ),
    # Main Dish
    path("main-dish/", views.main_dish, name="main_dish"),
    path("beef/", views.beef, name="beef"),
    path("chicken/", views.chicken, name="chicken"),
    path("fastfood/", views.fastfood, name="fastfood"),
    path("pasta/", views.pasta, name="pasta"),
    path("seafood/", views.seafood, name="seafood"),
    path("vegetarian/", views.vegetarian, name="vegetarian"),
    # Favorites
    path('favorites/', views.favorites_list, name='favorites'),
    path('toggle/<int:item_id>/', views.toggle_favorite, name='toggle_favorite'),
]
