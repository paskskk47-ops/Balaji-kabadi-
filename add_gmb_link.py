import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Adding GMB directions and maps integration in: {base_dir}")

disclaimer_old = "based at Amrapali Circle, Vaishali Nagar, Jaipur 302021."
disclaimer_new = 'based at <a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" style="text-decoration: underline;">Amrapali Circle, Vaishali Nagar, Jaipur 302021</a>.'

contact_old = "<p><strong>Head Office Location:</strong><br>Amrapali Circle, Vaishali Nagar, Jaipur, Rajasthan 302021</p>"
contact_new = """<p><strong>Head Office Location:</strong><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" style="text-decoration: underline; color: var(--primary);">Amrapali Circle, Vaishali Nagar, Jaipur, Rajasthan 302021</a><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" class="btn btn-secondary" style="margin-top: 8px; padding: 6px 12px; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 5px;">📍 Get Directions on Google Maps</a></p>"""

jaipur_old = "<p><strong>Primary Address:</strong><br>Amrapali Circle, Vaishali Nagar, Jaipur, Rajasthan 302021</p>"
jaipur_new = """<p><strong>Primary Address:</strong><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" style="text-decoration: underline; color: var(--primary);">Amrapali Circle, Vaishali Nagar, Jaipur, Rajasthan 302021</a><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" class="btn btn-secondary" style="margin-top: 8px; padding: 6px 12px; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 5px;">📍 Get Directions on Google Maps</a></p>"""

scrap_buying_old = "<p><strong>HQ Address:</strong><br>Amrapali Circle, Vaishali Nagar, Jaipur, RJ 302021</p>"
scrap_buying_new = """<p><strong>HQ Address:</strong><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" style="text-decoration: underline; color: var(--primary);">Amrapali Circle, Vaishali Nagar, Jaipur, RJ 302021</a><br><a href="https://share.google/XoktDJaoK5XxPs7VD" target="_blank" rel="noopener" class="btn btn-secondary" style="margin-top: 8px; padding: 6px 12px; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 5px;">📍 Get Directions on Google Maps</a></p>"""

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            if ".git" in file_path or "assets" in file_path:
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            
            # Replace disclaimer footer
            if disclaimer_old in content:
                content = content.replace(disclaimer_old, disclaimer_new)
                
            # Replace local pages specific address fields
            if file == "contact.html" and contact_old in content:
                content = content.replace(contact_old, contact_new)
                
            if file == "jaipur.html" and jaipur_old in content:
                content = content.replace(jaipur_old, jaipur_new)
                
            if file == "scrap-buying-jaipur.html" and scrap_buying_old in content:
                content = content.replace(scrap_buying_old, scrap_buying_new)
                
            # Inject hasMap inside LocalBusiness schema
            schema_target = '"name": "Balaji Best Kabadi Wala",'
            schema_replacement = '"name": "Balaji Best Kabadi Wala",\n    "hasMap": "https://share.google/XoktDJaoK5XxPs7VD",'
            if schema_target in content and '"hasMap"' not in content:
                content = content.replace(schema_target, schema_replacement)
                
            if content != original_content:
                print(f"Added GMB maps integration in: {file_path}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("GMB Directions integration completed successfully!")
