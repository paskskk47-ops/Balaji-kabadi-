import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Injecting favicon link to HTML heads in: {base_dir}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Skip if inside .git or assets
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Skip if already has favicon link
            if 'rel="icon"' in content:
                continue
                
            # Determine path depth relative to base_dir
            rel_path = os.path.relpath(file_path, base_dir)
            depth = rel_path.count(os.sep)
            
            if depth == 0:
                favicon_href = "./favicon.svg"
            else:
                favicon_href = "../" * depth + "favicon.svg"
                
            favicon_tag = f'\n  <link rel="icon" type="image/svg+xml" href="{favicon_href}">'
            
            # Inject right after <head>
            if "<head>" in content:
                print(f"Injecting favicon in: {file_path} (href={favicon_href})")
                content = content.replace("<head>", f"<head>{favicon_tag}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Favicon injection completed successfully!")
