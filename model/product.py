from pathlib import Path
from data.constants import IMAGE_PATH, PRODUCTS_PATH, SVG_TEMPLATE
from modules.csv_module import read_products_csv, row_to_dict

class Replacement:
    def __init__(self, tag: str, type: str, value: str) -> None:
        self.tag = tag
        self.type = type
        self.value = value

class Product:
    def __init__(self, code: str, maker: str, brand: str, name: str, buy_price: float, sell_price: float, side: str, car1: str, car2: str, created: bool) -> None:
        self.code = code
        self.maker = maker
        self.brand = brand
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.side = side
        self.created = created
        self.image = f'{IMAGE_PATH}{self.code}.png'
        self.car1 = car1,
        self.car2 = car2
    
    @property
    def replacements(self) -> list:
        return [
            Replacement('--TITLE--', 'text', f'{self.name} {self.side}'),
            Replacement('--MODEL--', 'text', f'{self.maker} {self.brand}'),
            Replacement('--IMAGE--', 'image', self.image),
            Replacement('--CAR1--', 'text', self.car1),
            Replacement('--CAR2--', 'text', self.car2),
        ]
        
    @classmethod
    def get_products(cls, file: Path):
        df = read_products_csv(file)
        return [cls(**d) for d in row_to_dict(df)]