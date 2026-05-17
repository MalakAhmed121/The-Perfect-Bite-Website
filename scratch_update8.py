import os
import glob

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if "{% static 'js/favorites.js' %}" in content:
        # If the file already has bakery-java.js, just remove favorites.js
        if "{% static 'js/bakery-java.js' %}" in content:
            new_content = content.replace("<script src=\"{% static 'js/favorites.js' %}\"></script>", "")
        else:
            # Otherwise replace it with bakery-java.js
            new_content = content.replace("favorites.js", "bakery-java.js")
            
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1

print(f"Fixed favorites.js imports in {count} files.")
