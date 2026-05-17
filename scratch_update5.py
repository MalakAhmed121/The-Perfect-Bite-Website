import os
import glob
import re

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Ensure style.css is linked
    if 'href="{% static \'css/style.css\' %}"' not in content:
        # Find the first CSS link and insert style.css before it
        link_pattern = re.compile(r'<link\s+rel="stylesheet"\s+href="{% static \'css/[^\']+\.css\' %}"\s*/?>')
        match = link_pattern.search(content)
        if match:
            style_link = '<link rel="stylesheet" href="{% static \'css/style.css\' %}" />\n    '
            content = content[:match.start()] + style_link + content[match.start():]
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

print("Injected style.css into HTML files.")

# Now clean up CSS files
css_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\static\css"
css_files = [
    'Health_Style.css', 'appetizers.css', 'bakery-style.css',
    'dessert.css', 'drinks.css', 'maindish.css'
]

selectors_to_remove = [
    r'#navbar\s*\{[^}]*\}',
    r'\.main-nav\s*\{[^}]*\}',
    r'\.logo\s*\{[^}]*\}',
    r'\.nav-links\s*\{[^}]*\}',
    r'\.nav-links\s+li\s*\{[^}]*\}',
    r'\.nav-links\s+a\s*\{[^}]*\}',
    r'\.nav-links\s+a:hover\s*(?:,\s*\.nav-links\s+li\s+button#backbutton:hover\s*)?\{[^}]*\}',
    r'\.big-arrow-btn\s*\{[^}]*\}',
    r'\.big-arrow-btn:hover\s*\{[^}]*\}'
]

for css_file in css_files:
    filepath = os.path.join(css_dir, css_file)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        for selector in selectors_to_remove:
            content = re.sub(selector, '', content, flags=re.MULTILINE|re.DOTALL)
            
        # Optional cleanup of empty lines
        content = re.sub(r'\n\s*\n', '\n\n', content)
            
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
            
print("Cleaned up CSS files.")
