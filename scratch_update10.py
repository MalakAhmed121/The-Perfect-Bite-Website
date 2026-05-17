import os
import glob

base_dir = r"d:\web_course\The-Perfect-Bite-Website\backend\recipes\templates\recipes"
files = glob.glob(base_dir + "/**/*.html", recursive=True)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Check if there is a backslash before the quotes
    if r"{% static \'css/style.css\' %}" in content or r"{% static \'css/style.css\' %}" in content:
        # Note: in python r"\'" is literally backslash then quote
        bad_str = r"{% static \'css/style.css\' %}"
        good_str = "{% static 'css/style.css' %}"
        if bad_str in content:
            new_content = content.replace(bad_str, good_str)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1

print(f"Fixed template syntax error in {count} files.")
