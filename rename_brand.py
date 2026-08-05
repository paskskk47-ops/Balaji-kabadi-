import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Renaming brand name to Balaji Best Kabadi Wala in: {base_dir}")

replacements = {
    "<span>Jaipur Scrap Guide</span>": "<span>Balaji Best Kabadi Wala</span>",
    "&copy; 2026 Jaipur Scrap Guide": "&copy; 2026 Balaji Best Kabadi Wala",
    "| Jaipur Scrap & Recycling Guide": "| Balaji Best Kabadi Wala",
    '<div class="logo-icon">J</div>': '<div class="logo-icon">B</div>',
    "Jaipur Scrap Guide Logo": "Balaji Best Kabadi Wala Logo",
    "Jaipur Scrap Guide. All rights reserved.": "Balaji Best Kabadi Wala. All rights reserved."
}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith((".html", ".xml", ".txt")):
            file_path = os.path.join(root, file)
            # Skip if file_path is inside .git or assets
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            
            for old_text, new_text in replacements.items():
                if old_text in content:
                    content = content.replace(old_text, new_text)
                    
            if content != original_content:
                print(f"Renamed brand in: {file_path}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Brand renaming completed successfully!")
