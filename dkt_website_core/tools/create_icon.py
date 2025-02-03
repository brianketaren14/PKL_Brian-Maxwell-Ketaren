from PIL import Image, ImageDraw, ImageFont
import os

def create_module_icon():
    # Buat direktori jika belum ada
    icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'description')
    os.makedirs(icon_path, exist_ok=True)
    
    # Buat gambar 140x140 dengan background putih
    size = (140, 140)
    img = Image.new('RGB', size, '#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    # Buat lingkaran biru sebagai background
    draw.ellipse([10, 10, 130, 130], fill='#1a73e8')
    
    # Tambah inisial "PK" di tengah dengan warna putih
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    text = "PK"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2
    
    draw.text((x, y), text, font=font, fill='white')
    
    # Simpan icon
    icon_file = os.path.join(icon_path, 'icon.png')
    img.save(icon_file)
    print(f"Icon created at: {icon_file}")

if __name__ == "__main__":
    create_module_icon() 