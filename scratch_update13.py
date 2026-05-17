import os

html_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero main tag to remove quotes inside url()
content = content.replace(
    '<main class="new-hero-section" style="background-image: url(\'{% static "premium_kitchen_hero.png" %}\');">',
    '<main class="new-hero-section" style="background-image: url({% static \'premium_kitchen_hero.png\' %});">'
)
content = content.replace(
    '<main class="new-hero-section" style="background-image: url(\'{% static "home-page.png" %}\');">',
    '<main class="new-hero-section" style="background-image: url({% static \'home-page.png\' %});">'
)

# Convert feature cards from <div> to <a>
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url "recipes" %}\'">',
    '<a href="{% url \'recipes\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url \"recipes\" %}\'">',
    '<a href="{% url \'recipes\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url "search" %}\'">',
    '<a href="{% url \'search\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url \"search\" %}\'">',
    '<a href="{% url \'search\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url "favorites" %}\'">',
    '<a href="{% url \'favorites\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)
content = content.replace(
    '<div class="feature-card" onclick="location.href=\'{% url \"favorites\" %}\'">',
    '<a href="{% url \'favorites\' %}" class="feature-card" style="text-decoration: none; display: block; color: inherit;">'
)

# Close the <a> tags instead of </div>
# Since each feature card ends with </p>\n            </div>, we can replace that
content = content.replace(
    '<p>Discover the recipes that are breaking the internet this week.</p>\n            </div>',
    '<p>Discover the recipes that are breaking the internet this week.</p>\n            </a>'
)
content = content.replace(
    '<p>Gourmet meals ready in under 15 minutes for your busy nights.</p>\n            </div>',
    '<p>Gourmet meals ready in under 15 minutes for your busy nights.</p>\n            </a>'
)
content = content.replace(
    '<p>Feeling cozy or adventurous? Find the perfect dish for your vibe.</p>\n            </div>',
    '<p>Feeling cozy or adventurous? Find the perfect dish for your vibe.</p>\n            </a>'
)

# Convert bento cards from <div> to <a> and fix background-image url() quotes
bento_cards = [
    ('main_dish', 'tall', 'maindish/main.jpg', 'Main Dishes'),
    ('healthy', '', 'Healthy_images/healthy_food.jpg', 'Healthy Food'),
    ('bakery', 'tall', 'bakeryimages/bakery12.png', 'Bakery'),
    ('dessert', '', 'dessertimages/background.jpg', 'Desserts'),
    ('juices', '', 'drinksimages/juices.jpeg', 'Juices'),
    ('appetizers', '', 'appetizersimgs/main1.jpg', 'Appetizers')
]

for url_name, card_class, img_path, title in bento_cards:
    class_str = f"bento-card {card_class}".strip()
    
    # Locate the old div pattern
    # It might have different quotes, so let's do a regex-free approach or generic replace
    old_div_pattern1 = f'<div class="{class_str}" style="background-image: url(\'{{\% static "{img_path}" \%}}\');" onclick="location.href=\'{{\% url "{url_name}" \%}}\'">'
    old_div_pattern2 = f'<div class="{class_str}" style="background-image: url(\'{{\% static \'{img_path}\' \%}}\');" onclick="location.href=\'{{\% url \'{url_name}\' \%}}\'">'
    
    new_a_tag = f'<a href="{{% url \'{url_name}\' %}}" class="{class_str}" style="background-image: url({{% static \'{img_path}\' %}}); text-decoration: none;">'
    
    # We will search and replace dynamically based on what's in the file
    # Let's write a targeted replace
    # We know the style and onclick are there, let's just match the start of the bento-card divs
    
# Let's do a simpler text replace of the whole bento grid section to be 100% clean
bento_grid_section_old = """        <div class="bento-grid">
            <div class="bento-card tall" style="background-image: url('{% static "maindish/main.jpg" %}');" onclick="location.href='{% url "main_dish" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Main Dishes</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card" style="background-image: url('{% static "Healthy_images/healthy_food.jpg" %}');" onclick="location.href='{% url "healthy" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Healthy Food</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card tall" style="background-image: url('{% static "bakeryimages/bakery12.png" %}');" onclick="location.href='{% url "bakery" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Bakery</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
            
            <div class="bento-card" style="background-image: url('{% static "dessertimages/background.jpg" %}');" onclick="location.href='{% url "dessert" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Desserts</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>

            <div class="bento-card" style="background-image: url('{% static "drinksimages/juices.jpeg" %}');" onclick="location.href='{% url "juices" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Juices</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>

            <div class="bento-card" style="background-image: url('{% static "appetizersimgs/main1.jpg" %}');" onclick="location.href='{% url "appetizers" %}'">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Appetizers</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </div>
        </div>"""

bento_grid_section_new = """        <div class="bento-grid">
            <a href="{% url 'main_dish' %}" class="bento-card tall" style="background-image: url({% static 'maindish/main.jpg' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Main Dishes</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>
            
            <a href="{% url 'healthy' %}" class="bento-card" style="background-image: url({% static 'Healthy_images/healthy_food.jpg' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Healthy Food</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>
            
            <a href="{% url 'bakery' %}" class="bento-card tall" style="background-image: url({% static 'bakeryimages/bakery12.png' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Bakery</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>
            
            <a href="{% url 'dessert' %}" class="bento-card" style="background-image: url({% static 'dessertimages/background.jpg' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Desserts</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>

            <a href="{% url 'juices' %}" class="bento-card" style="background-image: url({% static 'drinksimages/juices.jpeg' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Juices</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>

            <a href="{% url 'appetizers' %}" class="bento-card" style="background-image: url({% static 'appetizersimgs/main1.jpg' %}); text-decoration: none;">
                <div class="bento-overlay"></div>
                <div class="bento-content">
                    <h3>Appetizers</h3>
                    <button class="bento-btn">View Recipes</button>
                </div>
            </a>
        </div>"""

# Replace the whole section
content = content.replace(bento_grid_section_old, bento_grid_section_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed quotes and refactored code to semantic <a> tags.")
