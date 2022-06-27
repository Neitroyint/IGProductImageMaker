from pathlib import Path
from classes.product import Product
from data.constants import PRODUCTS_PATH, RESULT_PATH, TEST_REPLACEMENT_DATA
from modules.csv_module import read_csv
from modules.image_module import generate_images

def execute():
    csv_file = Path(PRODUCTS_PATH)
    result_path = Path(RESULT_PATH)
    products = [p for p in Product.get_products(csv_file) if not p.created]
    generate_images(products)
    

if __name__ == "__main__":
    execute()