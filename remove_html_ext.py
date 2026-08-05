import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Removing .html extensions from URLs in: {base_dir}")

# We want to replace links in href="..." and urls in loc tags of sitemap, canonical links, etc.
# 1. href=".../something.html" -> href=".../something"
# 2. <loc>.../something.html</loc> -> <loc>.../something</loc>
# 3. href="something.html" -> href="something"
# 4. "item": ".../something.html" -> "item": ".../something" (in JSON-LD)

# We can use regex to find files referencing .html:
href_pattern = re.compile(r'href="([^"]+)\.html"')
loc_pattern = re.compile(r'<loc>([^<]+)\.html</loc>')
item_pattern = re.compile(r'"item":\s*"([^"]+)\.html"')

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
            
            # Replace hrefs
            content = href_pattern.sub(r'href="\1"', content)
            
            # Replace sitemap locs
            content = loc_pattern.sub(r'<loc>\1</loc>', content)
            
            # Replace JSON-LD items
            content = item_pattern.sub(r'"item": "\1"', content)
            
            if content != original_content:
                print(f"Cleaned URLs in: {file_path}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print(".html removal from URLs completed successfully!")
