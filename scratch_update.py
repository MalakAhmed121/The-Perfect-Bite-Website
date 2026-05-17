import os
import glob

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

target_html1 = """            <div class="menu-icon">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>"""

target_html2 = """<div class="menu-icon">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>"""

replacement_html = """            <div class="nav-left">
                <!-- Back Button -->
                <button class="nav-back-btn" onclick="window.history.back()" aria-label="Go Back">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="12" x2="5" y2="12"></line>
                        <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    <span>Back</span>
                </button>
                <!-- Menu Icon -->
                <div class="menu-icon">
                    <div class="bar"></div>
                    <div class="bar"></div>
                    <div class="bar"></div>
                </div>
            </div>"""

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    if target_html1 in content:
        content = content.replace(target_html1, replacement_html)
        modified = True
    elif target_html2 in content:
        content = content.replace(target_html2, replacement_html)
        modified = True
        
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print(f"Modified {count} files.")
