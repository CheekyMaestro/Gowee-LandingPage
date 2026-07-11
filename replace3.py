import re
import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

image_map = {
    'velvet blue': 'VelvetBlue.png',
    'velvet': 'Velvet.png',
    'only her': 'OnlyHer.png',
    'gorgeous': 'Gorgeous.png',
    'sunset tropic': 'SunsetTropic.png',
    'johnny': 'Johny.png',
    'fernando': 'Fernando.png',
    'velvet elixir': 'VelvetElixir.png',
    'sunset rouge': 'SunsetRogue.png',
    'after midnight': 'AfterMidnight.png',
    'sunshine': 'Sunshine.png',
    'shocked': 'Shocked.png',
    'visca': 'Visca.png'
}

# Find all comments
pattern = r'<!-- GANTI src DI BAWAH INI DENGAN FOTO ASLI PRODUK:\s*(.*?)\s*-->'
matches = list(re.finditer(pattern, content))

offset = 0
new_content = ""
last_idx = 0

for match in matches:
    product_name = match.group(1).strip().lower()
    
    # We always append up to the end of the comment
    new_content += content[last_idx:match.end()]
    last_idx = match.end()
    
    if product_name in image_map:
        filename = image_map[product_name]
        
        # Look for the next src="..." after this comment
        # It should be within the next 500 characters
        search_area = content[match.end():match.end()+500]
        src_match = re.search(r'src="[^"]*"', search_area)
        
        if src_match:
            # Append everything up to the src="
            new_content += search_area[:src_match.start()]
            # Append the new src
            new_content += f'src="{filename}"'
            # Update last_idx
            last_idx = match.end() + src_match.end()

# Append the rest of the file
new_content += content[last_idx:]

# Also replace the hero image which doesn't have the exact same comment structure, just in case
# Wait, hero image comment:
# <!-- GANTI src DI ATAS DENGAN FOTO PRODUK UNGGULAN GOWWEE (background transparan/menyatu) begitu foto asli tersedia -->
# But it's already Gorgeous.png on line 284.

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Images replaced reliably.")
