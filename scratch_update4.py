import os
import glob
import re

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

script_tag = "<script src=\"{% static 'js/main.js' %}\"></script>"

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if main.js is already included
    if 'main.js' not in content:
        # Insert before </body>
        if '</body>' in content:
            new_content = content.replace('</body>', f'    {script_tag}\n</body>')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1

print(f"Added main.js to {count} files.")
