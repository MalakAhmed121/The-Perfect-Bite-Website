import os
import glob
import re

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Check if there's a commented out style.css
    comment_pattern = re.compile(r'<!--\s*<link rel="stylesheet" href="{% static \'css/style.css\' %}"\s*/?>\s*-->')
    if comment_pattern.search(content):
        # Uncomment it
        new_content = comment_pattern.sub(r'<link rel="stylesheet" href="{% static \'css/style.css\' %}" />', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
    # Check if it doesn't have it at all or it's still commented but different formatting
    elif 'href="{% static \'css/style.css\' %}"' not in content.replace('<!--', ''):
        link_pattern = re.compile(r'<link\s+rel="stylesheet"\s+href="{% static \'css/[^\']+\.css\' %}"\s*/?>')
        match = link_pattern.search(content)
        if match:
            style_link = '<link rel="stylesheet" href="{% static \'css/style.css\' %}" />\n    '
            content = content[:match.start()] + style_link + content[match.start():]
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            count += 1

print(f"Uncommented/Added style.css in {count} files.")
