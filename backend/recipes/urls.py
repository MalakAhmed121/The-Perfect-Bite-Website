from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cover/", views.cover, name="cover"),
    path("favorites/", views.favorites, name="favorites"),
    path("recipes/", views.recipes_page, name="recipes"),
    path('search/', views.search_page, name='search'),
    path('ajax-search/', views.ajax_search, name='ajax_search'),
    
    path("recipe/<slug:slug>/", views.recipe_details, name="recipe_detail"),
    
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    path("logout/", views.logout_user, name="logout"),
    
    path("add-recipe/", views.add_recipe, name="add_recipe"),
    path("edit-recipe/<int:id>/", views.edit_recipe, name="edit_recipe"),
    path("delete-recipe/<int:id>/", views.delete_recipe, name="delete_recipe"),
    path("view-recipe/<int:id>/", views.view_recipe, name="view_recipe"),
    path("category/healthy/", views.category_detail, {'category_name': 'healthy'}, name="healthy"),
    path("category/<str:category_name>/", views.category_detail, name="category_detail"),
    
    path("main-dish/", views.category_detail, {'category_name': 'Main Dish'}, name="main_dish"),
    path("beef/", views.category_detail, {'category_name': 'Beef'}, name="beef"),
    path("chicken/", views.category_detail, {'category_name': 'Chicken'}, name="chicken"),
    path("fastfood/", views.category_detail, {'category_name': 'Fast Food'}, name="fastfood"),
    path("fast-food/", views.category_detail, {'category_name': 'Fast Food'}, name="fast_food"),
    path("seafood/", views.category_detail, {'category_name': 'Seafood'}, name="seafood"),
    path("appetizers/", views.category_detail, {'category_name': 'Appetizers'}, name="appetizers"),
    path("bakery/", views.category_detail, {'category_name': 'Bakery'}, name="bakery"),
    path("dessert/", views.category_detail, {'category_name': 'Dessert'}, name="dessert"),
    
    # Bakery Sub-categories
    path("bread/", views.category_detail, {'category_name': 'Bread'}, name="bread"),
    path("croissants/", views.category_detail, {'category_name': 'Croissants'}, name="croissants"),
    path("cookies/", views.category_detail, {'category_name': 'Cookies'}, name="cookies"),
    path("macarons/", views.category_detail, {'category_name': 'Macarons'}, name="macarons"),
    path("macrons/", views.category_detail, {'category_name': 'Macarons'}, name="macrons"),
    path("donuts/", views.category_detail, {'category_name': 'Donuts'}, name="donuts"),
    path("cinnamon/", views.category_detail, {'category_name': 'Cinnamon'}, name="cinnamon"),

    # Drinks & Beverages
    path("drinks/", views.category_detail, {'category_name': 'Drinks'}, name="drinks"),
    path("coffee/", views.category_detail, {'category_name': 'Coffee'}, name="coffee"),
    path("juices/", views.category_detail, {'category_name': 'Juices'}, name="juices"),
    path("hot-drinks/", views.category_detail, {'category_name': 'Hot Drinks'}, name="hot_drinks"),
    path("hot_drinks/", views.category_detail, {'category_name': 'Hot Drinks'}, name="hot_drinks_alt"),

    # Main Dish Sub-categories
    path("pasta/", views.category_detail, {'category_name': 'Pasta'}, name="pasta"),
    path("vegetarian/", views.category_detail, {'category_name': 'Vegetarian'}, name="vegetarian"),

    path("toggle-favorite/<int:recipe_id>/", views.toggle_favorite, name="toggle_favorite"),
    path("recipe-api/<int:recipe_id>/", views.recipe_api, name="recipe_api"),
    
    path("admin-recipe/", views.admin_recipe, name="admin_recipe"),
]
