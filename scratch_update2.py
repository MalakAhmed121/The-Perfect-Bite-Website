import os
import glob
import re

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

back_button_html = """            <div class="nav-left">
                <!-- Back Button -->
                <button class="nav-back-btn" onclick="window.history.back()" aria-label="Go Back">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="12" x2="5" y2="12"></line>
                        <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    <span>Back</span>
                </button>
            </div>"""

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'class="nav-left"' in content:
        continue # Already modified
        
    pattern = r'(<nav[^>]*class="main-nav"[^>]*>)'
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\1\n' + back_button_html, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1

print(f"Modified {count} files.")
