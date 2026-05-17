import os
import re

css_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\static\css"
files_colors = {
    'Health_Style.css': '#27ae60',
    'appetizers.css': '#C1772B',
    'bakery-style.css': '#4b1f11',
    'dessert.css': '#6B3E26',
    'maindish.css': '#A98F6F'
}

for filename, color in files_colors.items():
    filepath = os.path.join(css_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '--primary-color' not in content:
            # Check if :root exists
            if ':root' in content:
                # Add inside :root
                content = re.sub(r':root\s*\{', f':root {{\n    --primary-color: {color};', content, count=1)
            else:
                # Add :root at the top
                content = f":root {{\n    --primary-color: {color};\n}}\n" + content
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
print("Injected --primary-color into category CSS files.")
