import fitz
import os
from PIL import Image, ImageDraw

pdf_path = r'C:\Users\Dinesh\Documents\Downloads\SAVIT Catalogue rev5.pdf'
out_dir = r'C:\Users\Dinesh\AppData\Local\Temp\opencode\savit-sustainables\images'
prod_dir = os.path.join(out_dir, 'products')
os.makedirs(prod_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Page 1 -> Logo (crop top 25%)
page = doc[0]
pix = page.get_pixmap(dpi=200)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
logo = img.crop((0, 0, pix.width, int(pix.height * 0.25)))
logo.save(os.path.join(out_dir, 'logo.webp'), 'WEBP', quality=85)
print('Logo saved')

# Page 1 full -> hero-image
pix = page.get_pixmap(dpi=150)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
img.save(os.path.join(out_dir, 'hero-image.webp'), 'WEBP', quality=80)
print('Hero image saved')

# Page 2 -> about-image
page = doc[1]
pix = page.get_pixmap(dpi=150)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
img.save(os.path.join(out_dir, 'about-image.webp'), 'WEBP', quality=80)
print('About image saved')

# Page 1 resized -> og-image
page = doc[0]
pix = page.get_pixmap(dpi=100)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
img = img.resize((1200, 630))
img.save(os.path.join(out_dir, 'og-image.webp'), 'WEBP', quality=85)
print('OG image saved')

# Product pages mapping
products = {
    3: 'bamboo-drinkware',
    4: 'bamboo-stationery',
    5: 'jute-bags',
    7: 'eco-goods',
    8: 'eco-cutlery',
}
for pnum, pname in products.items():
    page = doc[pnum - 1]
    pix = page.get_pixmap(dpi=150)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    img.save(os.path.join(prod_dir, f'{pname}.webp'), 'WEBP', quality=80)
    print(f'{pname}.webp saved')

# Personal care - page 9 (neem combs)
page = doc[8]
pix = page.get_pixmap(dpi=150)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
img.save(os.path.join(prod_dir, 'personal-care.webp'), 'WEBP', quality=80)
print('personal-care.webp saved')

# Corporate kits - page 6
page = doc[5]
pix = page.get_pixmap(dpi=150)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
img.save(os.path.join(prod_dir, 'corporate-kits.webp'), 'WEBP', quality=80)
print('corporate-kits.webp saved')

# Compostable bags - create placeholder
placeholder = Image.new('RGB', (640, 480), (27, 94, 59))
draw = ImageDraw.Draw(placeholder)
draw.text((200, 220), 'Compostable Bags', fill=(168, 213, 181))
placeholder.save(os.path.join(prod_dir, 'compostable-bags.webp'), 'WEBP', quality=80)
print('compostable-bags.webp saved (placeholder)')

# Favicon from logo
logo_small = logo.resize((32, 32))
logo_small.save(os.path.join(out_dir, 'favicon.ico'), 'ICO', sizes=[(32, 32)])
print('favicon.ico saved')

print('All images created successfully')
