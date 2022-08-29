import base64
from pathlib import Path
from numpy import byte, void
from wand.image import Image
from wand.font import Font
from classes.product import Product
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

from data.constants import FONT_TYPES, RESULT_PATH, SVG_TEMPLATE

def get_template_data() -> str:
    template_path = Path(SVG_TEMPLATE)
    with open(template_path, 'r', encoding='cp1252') as base:
        data = base.read()
    return data

def change_svg_data(template: str, replacements: list) -> bytes:
    for t in FONT_TYPES:
        template = template.replace(f'-{t}', '')
        template = template.replace(f' - {t}', '')
        template = template.replace(f'- {t}', '')
        template = template.replace(f' -{t}', '')
        template = template.replace(f'{t}', '')
        template = template.replace(f' {t}', '')
    for r in replacements:
        if r.type == 'image':
            r.value = img_to_base64(r.value)
        template = template.replace(r.tag, str(r.value))
    return template

def img_to_base64(image: Path) -> str:
    with open(image, 'rb') as img:
        b64_str = base64.b64encode(img.read()).decode("utf-8")
    return b64_str

def generate_image(product: Product) -> void:
    data = change_svg_data(get_template_data(), product.replacements)
    with open(f'{RESULT_PATH}\\{product.code}.svg', 'w') as svg:
        svg.write(data)
    with Image(filename=f'{RESULT_PATH}\\{product.code}.svg', width=1080, height=1080, format='svg') as img:
        png_image = img.make_blob('png')
        f = open(f'{RESULT_PATH}\\{product.code}.png', "wb")
        f.write(png_image)
        f.close()
        # with img.convert('png') as output_img:
        #     output_img.save(filename=f'{RESULT_PATH}\\{product.code}.png')

def generate_images(products: list) -> void:
    for p in products:
        generate_image(p)

    
        
    