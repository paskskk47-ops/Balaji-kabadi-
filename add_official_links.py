import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Adding official website backlinks to all pages in: {base_dir}")

backlink_box = """
        <!-- Contextual Backlink to Official Site -->
        <div class="details-box" style="background-color: var(--primary-light); border-left: 4px solid var(--primary); padding: 1.5rem; margin: 1.5rem 0;">
          <p>🔗 <strong>Official Website:</strong> For real-time daily rates, live estimations, and direct bookings, visit the <a href="https://balajibestkabadiwala.in/" target="_blank" rel="noopener" style="text-decoration: underline; font-weight: 700;">Official Balaji Best Kabadi Wala Website</a>.</p>
        </div>
"""

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Skip if file_path is inside .git, assets, or index.html (which already has specific links)
            if ".git" in file_path or "assets" in file_path or file == "404.html":
                continue
                
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Skip if it already has this specific backlink box or the link
            if "Official Balaji Best Kabadi Wala Website" in content:
                continue
                
            # Find the inline-whatsapp-box and insert the backlink right before it
            if "inline-whatsapp-box" in content:
                print(f"Adding official backlink box to: {file_path}")
                content = content.replace('<!-- Inline WhatsApp CTA Box -->', f'{backlink_box}\n\n        <!-- Inline WhatsApp CTA Box -->')
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

print("Official backlinks addition completed successfully!")
