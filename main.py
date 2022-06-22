from pathlib import Path
from classes.product import Product
from data.constants import PRODUCTS_PATH, RESULT_PATH, TEST_REPLACEMENT_DATA
from modules.csv_module import read_csv

def execute():
    csv_file = Path(PRODUCTS_PATH)
    result_path = Path(RESULT_PATH)
    products = [p for p in Product.get_products(csv_file) if not p.created]
    for p in products:
        p.generate_image(result_path)
    

if __name__ == "__main__":
    execute()
    # replacements = TEST_REPLACEMENT_DATA
    # svg_path = str(Path("./templates/base.svg"))
    
    # with open(svg_path, 'r', encoding='cp1252') as svg:
    #     data = svg.read()
    #     for r in replacements:
    #         data = data.replace(r, replacements[r])
    #     open('new_test.svg', 'w').write(data)

    # with Image(filename='new_test.svg', width=1080, height=1080) as img:
    #     img.font('./source/Monerd-Solid.ttf')
    #     with img.convert('png') as output_img:
    #         output_img.save(filename='new_image.png')