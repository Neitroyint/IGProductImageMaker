from pathlib import Path
from data.constants import IS_WIPE_DATA, OUT_IMA_PATH, OUT_SVG_PATH, OUTPUT_PATH, TEMP_PATH
from modules.path_module import create_output_dir, get_all_templates, wipe_data

def execute() -> None:
    out_path = Path(OUTPUT_PATH)
    
    if IS_WIPE_DATA:
        wipe_data(out_path)
        
    dir_list = [
        OUT_IMA_PATH, 
        OUT_SVG_PATH,
    ]
    create_output_dir(dir_list)
    
    temps = get_all_templates(TEMP_PATH)
    print("Please enter a number of the desire template:")
    for i in range(len(temps)):
        print(f'{str(i+1)}: {temps[i]}')
    option = int(input("Option: "))
    # csv_file = Path(PRODUCTS_PATH)
    # products = [p for p in Product.get_products(csv_file) if not p.created]
    # generate_images(products)

menu = {
    1: {
        "Text": "Run all steps",
        "Call": execute
    } 
}        

def run_menu():
    try:
        print("Please enter a number with the desired step:")
        for m in menu:
            print(f'{str(m)}: {menu[m]["Text"]}')
        option = int(input("Option: "))
        
        if option in menu:
            menu[option]["Call"]()
        else:
            print("Option selected was not available")
    except Exception as ex:
        print(ex)