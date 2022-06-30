from pathlib import Path
from classes.product import Product
from data.constants import PRODUCTS_PATH
from modules.image_module import generate_images

def execute():
    csv_file = Path(PRODUCTS_PATH)
    products = [p for p in Product.get_products(csv_file) if not p.created]
    generate_images(products)
    

if __name__ == "__main__":
    execute()