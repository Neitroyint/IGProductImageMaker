from pathlib import Path
from wand.image import Image

from data.constants import SVG_TEMPLATE

def get_template_data() -> str:
    template_path = Path(SVG_TEMPLATE)
    with open(template_path, 'r', encoding='cp1252') as base:
        data = base.read()
    return data

def change_svg_data(template: str, replacements: list) -> str:
    for r in replacements:
        data = data.replace(r, replacements[r])