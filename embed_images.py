import base64
import os

def get_base64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

logo_b64 = f"data:image/webp;base64,{get_base64('logo.webp')}"
caeti_b64 = f"data:image/webp;base64,{get_base64('assets/images/caeti.webp')}"

files_to_patch = ['index.html', 'test_certificate.html']

for filename in files_to_patch:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace logo.webp
    content = content.replace('src="logo.webp"', f'src="{logo_b64}"')
    # Replace assets/images/caeti.webp
    content = content.replace('src="assets/images/caeti.webp"', f'src="{caeti_b64}"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {filename}")
