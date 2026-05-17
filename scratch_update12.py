import os

html_path = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix image paths
content = content.replace("healthyfoodimgs/main.jpg", "Healthy_images/healthy_food.jpg")
content = content.replace("juicesimg/juicesbg.jpeg", "drinksimages/juices.jpeg")

# Fix quotes inside style and onclick attributes to satisfy IDE
# Replace 'static '...' ' with 'static "..." '
content = content.replace("url('{% static 'home-page.png' %}')", "url('{% static \"home-page.png\" %}')")
content = content.replace("url('{% static 'maindish/main.jpg' %}')", "url('{% static \"maindish/main.jpg\" %}')")
content = content.replace("url('{% static 'Healthy_images/healthy_food.jpg' %}')", "url('{% static \"Healthy_images/healthy_food.jpg\" %}')")
content = content.replace("url('{% static 'bakeryimages/bakery12.png' %}')", "url('{% static \"bakeryimages/bakery12.png\" %}')")
content = content.replace("url('{% static 'dessertimages/background.jpg' %}')", "url('{% static \"dessertimages/background.jpg\" %}')")
content = content.replace("url('{% static 'drinksimages/juices.jpeg' %}')", "url('{% static \"drinksimages/juices.jpeg\" %}')")
content = content.replace("url('{% static 'appetizersimgs/main1.jpg' %}')", "url('{% static \"appetizersimgs/main1.jpg\" %}')")

# Fix url name quotes in onclick
content = content.replace("onclick=\"location.href='{% url 'recipes' %}'\"", "onclick=\"location.href='{% url \"recipes\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'search' %}'\"", "onclick=\"location.href='{% url \"search\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'favorites' %}'\"", "onclick=\"location.href='{% url \"favorites\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'main_dish' %}'\"", "onclick=\"location.href='{% url \"main_dish\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'healthy' %}'\"", "onclick=\"location.href='{% url \"healthy\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'bakery' %}'\"", "onclick=\"location.href='{% url \"bakery\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'dessert' %}'\"", "onclick=\"location.href='{% url \"dessert\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'juices' %}'\"", "onclick=\"location.href='{% url \"juices\" %}'\"")
content = content.replace("onclick=\"location.href='{% url 'appetizers' %}'\"", "onclick=\"location.href='{% url \"appetizers\" %}'\"")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax and paths in index.html.")
