import os
import glob
import re

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

# Regex to find the <button class="nav-back-btn" ...> ... </button>
btn_pattern = re.compile(r'(\s*<button class="nav-back-btn"[^>]*>.*?</button>)', re.DOTALL)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Find the nav-right div
    if '<div class="nav-right">' in content:
        # Check if the button exists
        match = btn_pattern.search(content)
        if match:
            btn_html = match.group(1)
            # Remove the button from its current position
            new_content = content.replace(btn_html, '')
            # Insert the button immediately after <div class="nav-right">
            new_content = new_content.replace('<div class="nav-right">', f'<div class="nav-right">{btn_html}')
            
            # Write back only if changed
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                count += 1

print(f"Moved Back Button in {count} files.")
