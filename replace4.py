import re

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

pattern = r'<!-- GANTI src DI BAWAH INI DENGAN FOTO ASLI PRODUK:\s*(.*?)\s*-->'
matches = list(re.finditer(pattern, content))

offset = 0
new_content = ""
last_idx = 0

for match in matches:
    product_name = match.group(1).strip().lower()
    
    new_content += content[last_idx:match.end()]
    last_idx = match.end()
    
    if product_name in image_map:
        filename = image_map[product_name]
        
        # Give a large enough window to find the entire src attribute
        search_area = content[match.end():match.end()+5000]
        src_match = re.search(r'src="[^"]*"', search_area)
        
        if src_match:
            new_content += search_area[:src_match.start()]
            new_content += f'src="{filename}"'
            last_idx = match.end() + src_match.end()

new_content += content[last_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Images properly replaced.")
