import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Adding Designed By link to footer in: {base_dir}")

target_old = """    <div class="container footer-bottom">
      <p>&copy; 2026 Balaji Best Kabadi Wala. All rights reserved.</p>
      <p>Associated with <a href="https://balajibestkabadiwala.in/" target="_blank" rel="noopener" style="text-decoration: underline;">Balaji Best Kabadi Wala</a></p>
    </div>"""

target_new = """    <div class="container footer-bottom">
      <p>&copy; 2026 Balaji Best Kabadi Wala. All rights reserved.</p>
      <p style="margin: 0; text-align: center;">Designed by <a href="https://orbyza.com/" target="_blank" rel="noopener" style="text-decoration: underline;">Orbyza Digital Marketing Agency</a></p>
      <p>Associated with <a href="https://balajibestkabadiwala.in/" target="_blank" rel="noopener" style="text-decoration: underline;">Balaji Best Kabadi Wala</a></p>
    </div>"""

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Skip if file_path is inside .git or assets
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            if target_old in content:
                print(f"Injecting agency link in: {file_path}")
                content = content.replace(target_old, target_new)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Agency footer link injection completed successfully!")
