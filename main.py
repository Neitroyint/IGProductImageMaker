from pathlib import Path
from wand.image import Image

from data.constants import TEST_REPLACEMENT_DATA




if __name__ == "__main__":
    replacements = TEST_REPLACEMENT_DATA
    svg_path = str(Path("./templates/base.svg"))
    
    with open(svg_path, 'r', encoding='cp1252') as svg:
        data = svg.read()
        for r in replacements:
            data = data.replace(r, replacements[r])
        open('new_test.svg', 'w').write(data)

    with Image(filename='new_test.svg', width=1080, height=1080) as img:
        img.font('./source/Monerd-Solid.ttf')
        with img.convert('png') as output_img:
            output_img.save(filename='new_image.png')