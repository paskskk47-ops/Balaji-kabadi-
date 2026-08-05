import os

base_dir = os.path.dirname(os.path.abspath(__file__))
old_host = "https://balajikabadiwalajaipur.github.io/"
new_host = "https://paskskk47-ops.github.io/Balaji-kabadi-/"

print(f"Updating host from {old_host} to {new_host} in: {base_dir}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith((".html", ".xml", ".txt")):
            file_path = os.path.join(root, file)
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            if old_host in content:
                print(f"Updating: {file_path}")
                content = content.replace(old_host, new_host)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Host update completed successfully!")
