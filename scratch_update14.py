import os

html_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes\index.html"
css_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\static\css\style.css"

# 1. Clean index.html from all inline background styles
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero main tag
html = html.replace(
    '<main class="new-hero-section" style="background-image: url({% static \'premium_kitchen_hero.png\' %});">',
    '<main class="new-hero-section">'
)
html = html.replace(
    '<main class="new-hero-section" style="background-image: url({% static \'home-page.png\' %});">',
    '<main class="new-hero-section">'
)

# Replace bento cards tags to use dedicated classes instead of inline styles
html = html.replace(
    '<a href="{% url \'main_dish\' %}" class="bento-card tall" style="background-image: url({% static \'maindish/main.jpg\' %}); text-decoration: none;">',
    '<a href="{% url \'main_dish\' %}" class="bento-card bento-main-dish tall" style="text-decoration: none;">'
)
html = html.replace(
    '<a href="{% url \'healthy\' %}" class="bento-card" style="background-image: url({% static \'Healthy_images/healthy_food.jpg\' %}); text-decoration: none;">',
    '<a href="{% url \'healthy\' %}" class="bento-card bento-healthy" style="text-decoration: none;">'
)
html = html.replace(
    '<a href="{% url \'bakery\' %}" class="bento-card tall" style="background-image: url({% static \'bakeryimages/bakery12.png\' %}); text-decoration: none;">',
    '<a href="{% url \'bakery\' %}" class="bento-card bento-bakery tall" style="text-decoration: none;">'
)
html = html.replace(
    '<a href="{% url \'dessert\' %}" class="bento-card" style="background-image: url({% static \'dessertimages/background.jpg\' %}); text-decoration: none;">',
    '<a href="{% url \'dessert\' %}" class="bento-card bento-dessert" style="text-decoration: none;">'
)
html = html.replace(
    '<a href="{% url \'juices\' %}" class="bento-card" style="background-image: url({% static \'drinksimages/juices.jpeg\' %}); text-decoration: none;">',
    '<a href="{% url \'juices\' %}" class="bento-card bento-juices" style="text-decoration: none;">'
)
html = html.replace(
    '<a href="{% url \'appetizers\' %}" class="bento-card" style="background-image: url({% static \'appetizersimgs/main1.jpg\' %}); text-decoration: none;">',
    '<a href="{% url \'appetizers\' %}" class="bento-card bento-appetizers" style="text-decoration: none;">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Add relative background images to style.css
bento_css = """

/* Bento & Hero Background Images */
.new-hero-section {
    background-image: url("../premium_kitchen_hero.png");
}
.bento-main-dish {
    background-image: url("../maindish/main.jpg");
}
.bento-healthy {
    background-image: url("../Healthy_images/healthy_food.jpg");
}
.bento-bakery {
    background-image: url("../bakeryimages/bakery12.png");
}
.bento-dessert {
    background-image: url("../dessertimages/background.jpg");
}
.bento-juices {
    background-image: url("../drinksimages/juices.jpeg");
}
.bento-appetizers {
    background-image: url("../appetizersimgs/main1.jpg");
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(bento_css)

print("Migrated all backgrounds to CSS classes. HTML is completely clean!")
