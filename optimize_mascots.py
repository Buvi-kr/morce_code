import os
import io
import rembg
from PIL import Image

def process_image(in_path, out_path, size=(400, 400), quality=85):
    if not os.path.exists(in_path):
        print(f"Skipping: {in_path} (not found)")
        return

    print(f"Processing {in_path} -> {out_path}...")
    try:
        with open(in_path, 'rb') as i:
            # 1. Remove background using AI
            input_data = i.read()
            output_data = rembg.remove(input_data)
            
            # 2. Open as PIL image
            img = Image.open(io.BytesIO(output_data)).convert("RGBA")
            
            # 3. Resize
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # 4. Save as Optimized WebP
            img.save(out_path, 'WEBP', quality=quality)
            print(f"Success! Saved to {out_path}")
    except Exception as e:
        print(f"Error processing {in_path}: {e}")

# Process Mascots
mascots = ['dogi', 'raebi', 'caeti']
for m in mascots:
    process_image(f'assets/images/{m}.png', f'assets/images/{m}.webp')

# Process Logo
process_image('logo.png', 'logo.webp', size=(500, 500), quality=90)
