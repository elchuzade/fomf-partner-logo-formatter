import os
from PIL import Image
from PIL import ImageFilter
import cairosvg
import xml.etree.ElementTree as ET

# Create an output directory if it doesn't exist
output_dir = "processed_logos"
os.makedirs(output_dir, exist_ok=True)

def get_svg_size(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    width = root.get('width')
    height = root.get('height')

    # Handle units like "px" or percentages
    def parse_dimension(dim):
        if dim is None:
            return None
        if dim.endswith('px'):
            return float(dim[:-2])
        try:
            return float(dim)
        except:
            return None

    w = parse_dimension(width)
    h = parse_dimension(height)

    # If width or height is missing, default to 300x220
    if w is None or h is None:
        return (300, 220)
    return (w, h)


def convert_svg_to_png(svg_path, temp_png_path, max_width=260, max_height=180):
    w, h = get_svg_size(svg_path)

    # Calculate scale factor to fit inside max_width x max_height keeping aspect ratio
    scale_w = max_width / w
    scale_h = max_height / h
    scale = min(scale_w, scale_h)

    output_width = int(w * scale)
    output_height = int(h * scale)

    cairosvg.svg2png(
        url=svg_path,
        write_to=temp_png_path,
        output_width=output_width,
        output_height=output_height
    )


def process_logo(input_path, output_path, target_size=(300, 220), background_color=(255, 255, 255)):
    ext = os.path.splitext(input_path)[1].lower()

    if ext == ".svg":
        temp_png = input_path + ".temp.png"
        convert_svg_to_png(input_path, temp_png)
        image = Image.open(temp_png).convert("RGBA")
        os.remove(temp_png)
    else:
        image = Image.open(input_path).convert("RGBA")

    # Separate the alpha channel to detect transparency
    alpha = image.getchannel('A')
    bbox = alpha.getbbox()

    # Crop out transparent edges if any
    if bbox:
        image = image.crop(bbox)
        alpha = image.getchannel('A')  # Recalculate alpha after cropping

    # Paste on white background (to remove transparency)
    background = Image.new("RGBA", image.size, background_color + (255,))
    background.paste(image, mask=alpha)
    image = background.convert("RGB")

    # Resize image maintaining aspect ratio, but max width=260, max height=180
    logo_max_size = (260, 180)
    image.thumbnail(logo_max_size, Image.LANCZOS)

    image = image.filter(ImageFilter.SHARPEN)

    # Create a new white canvas
    canvas = Image.new("RGB", target_size, background_color)

    # Center the image on the canvas
    offset_x = (target_size[0] - image.width) // 2
    offset_y = (target_size[1] - image.height) // 2
    canvas.paste(image, (offset_x, offset_y))

    # Save the result as PNG
    canvas.save(output_path, format="PNG")
    print(f"✅ Processed: {output_path}")

# === Example Usage ===
if __name__ == "__main__":
    test_files = [
        # "test_logo.png",
        # "test_logo.jpg",
        # "test_logo.jpeg",
        # "test_logo.svg",
    ]

    for file in test_files:
        if os.path.exists(file):
            out_file = os.path.join(output_dir, os.path.splitext(file)[0] + "_processed.png")
            process_logo(file, out_file)
        else:
            print(f"⚠️ File not found: {file}")