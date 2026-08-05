import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Adding Robots Meta and Sitemap link to head in: {base_dir}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Skip if file_path is inside .git or assets
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Skip if already has robots meta
            if 'name="robots"' in content:
                continue
                
            print(f"Injecting meta tags in: {file_path}")
            
            # Determine robots content
            if file == "404.html":
                meta_tags = '\n  <meta name="robots" content="noindex, follow">'
            else:
                meta_tags = '\n  <meta name="robots" content="index, follow">'
                
            # Add Sitemap Link
            meta_tags += '\n  <link rel="sitemap" type="application/xml" title="Sitemap" href="https://paskskk47-ops.github.io/Balaji-kabadi-/sitemap.xml">'
            
            # Inject right after <head>
            if "<head>" in content:
                content = content.replace("<head>", f"<head>{meta_tags}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Robots and Sitemap link injection completed successfully!")
