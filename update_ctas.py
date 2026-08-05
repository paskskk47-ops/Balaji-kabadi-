import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

header_contact_html = """
      <div class="header-contact" style="margin-left: auto; margin-right: 1.5rem;">
        <a href="tel:+919509752549">📞 95097 52549</a>
        <a href="https://wa.me/919509752549" target="_blank" class="btn-whatsapp" style="padding: 6px 12px; font-size: 0.8rem; box-shadow: none; margin-left: 10px;">💬 WhatsApp</a>
      </div>
"""

rates_widget_template = """
        <!-- Live Scrap Rates Widget -->
        <div class="rates-widget">
          <h4 class="widget-title" style="border-bottom: 2px solid #25d366;">Aajke Scrap Rates</h4>
          <table class="rates-table">
            <thead>
              <tr>
                <th>Scrap Item</th>
                <th>Price Range</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>📰 Newspaper / Raddi</td>
                <td class="rates-highlight">₹17 - ₹18 / Kg</td>
              </tr>
              <tr>
                <td>📦 Cardboard / Carton</td>
                <td class="rates-highlight">₹13 / Kg</td>
              </tr>
              <tr>
                <td>🧴 Plastic Scrap</td>
                <td class="rates-highlight">₹12 / Kg</td>
              </tr>
              <tr>
                <td>🔩 Iron & Steel</td>
                <td class="rates-highlight">₹32 - ₹50 / Kg</td>
              </tr>
              <tr>
                <td>🪙 Copper Cable</td>
                <td class="rates-highlight">₹1150 / Kg</td>
              </tr>
              <tr>
                <td>🔋 Aluminium Scrap</td>
                <td class="rates-highlight">₹250 / Kg</td>
              </tr>
              <tr>
                <td>🔔 Brass / Pital</td>
                <td class="rates-highlight">₹750 / Kg</td>
              </tr>
              <tr>
                <td>💻 E-Waste (Laptops)</td>
                <td class="rates-highlight">₹200 - ₹300 / Unit</td>
              </tr>
              <tr>
                <td>⛓️ Mixed Metal</td>
                <td class="rates-highlight">₹13 / Kg</td>
              </tr>
            </tbody>
          </table>
          <p style="font-size: 0.75rem; color: var(--text-light); margin-top: 10px; text-align: center;">Rates updated daily in Jaipur. Free pickup included.</p>
          <a href="{contact_link}" class="btn btn-secondary" style="width: 100%; font-size: 0.85rem; padding: 8px; margin-top: 10px; display: inline-flex; align-items: center; justify-content: center; gap: 5px;">📞 Get Bulk Quote</a>
        </div>
"""

inline_whatsapp_box = """
        <!-- Inline WhatsApp CTA Box -->
        <div class="inline-whatsapp-box">
          <div class="inline-whatsapp-text">
            <h4>Ready to Sell Your Scrap?</h4>
            <p>Get instant doorstep weighing and on-the-spot UPI/Cash payout. Daily updated rates.</p>
          </div>
          <a href="https://wa.me/919509752549" target="_blank" rel="noopener" class="btn-whatsapp">💬 WhatsApp Rate Check</a>
        </div>
"""

whatsapp_float_html = """
  <!-- Floating WhatsApp CTA -->
  <a href="https://wa.me/919509752549" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">💬</a>
"""

print(f"Starting CTA and Rates updates in: {base_dir}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Skip if file_path is inside .git or assets
            if ".git" in file_path or "assets" in file_path:
                continue
                
            print(f"Updating: {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Determine path depth relative to base_dir
            rel_path = os.path.relpath(file_path, base_dir)
            depth = len(rel_path.split(os.sep)) - 1
            prefix = "../" * depth if depth > 0 else "./"
            contact_link = prefix + "contact.html"
            
            # 1. Update Header (only if not already updated)
            if "header-contact" not in content:
                # Find the logo block close tag and insert before button
                logo_pattern = re.compile(r'(<a\s+href="[^"]*index\.html"\s+class="logo">.*?</a>)', re.DOTALL)
                match = logo_pattern.search(content)
                if match:
                    logo_block = match.group(1)
                    new_logo_block = logo_block + "\n      " + header_contact_html.strip()
                    content = content.replace(logo_block, new_logo_block)
            
            # 2. Update Sidebar with Rates Widget (if sidebar exists and rates widget not already in it)
            if '<aside class="sidebar">' in content and "rates-widget" not in content:
                rates_widget_html = rates_widget_template.format(contact_link=contact_link).strip()
                content = content.replace('<aside class="sidebar">', f'<aside class="sidebar">\n        {rates_widget_html}')
                
            # 3. Update Article with Inline WhatsApp Box (if article exists and inline-whatsapp-box not already in it)
            if '</article>' in content and "inline-whatsapp-box" not in content:
                content = content.replace('</article>', f'{inline_whatsapp_box.strip()}\n      </article>')
                
            # 4. Add Floating WhatsApp Button (if not already present)
            if "whatsapp-float" not in content:
                content = content.replace('</body>', f'{whatsapp_float_html.strip()}\n\n</body>')
                
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

print("CTA and Rates updates completed successfully!")
