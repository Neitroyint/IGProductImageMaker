from pathlib import Path
from xmlrpc.client import Boolean
from data.constants import PRODUCTS_PATH
from modules.csv_module import read_csv, read_products_csv, row_to_dict

class Replacement:
    def __init__(self, tag: str, value: str) -> None:
        self.tag = tag
        self.value = value

class Product:
    def __init__(self, code: str, maker: str, brand: str, name: str, buy_price: float, sell_price: float, side: str, created: bool) -> None:
        self.code = code
        self.maker = maker
        self.brand = brand
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.side = side
        self.created = created
    
    @property
    def replacements(self) -> list:
        return [
            Replacement('--Title--', f'{self.name} {self.side}'),
            Replacement('--MODEL--', f'{self.maker} {self.brand}'),
            Replacement('--Title--', f'{self.name} {self.side}'),
            Replacement('--Title--', f'{self.name} {self.side}'),
            Replacement('--Title--', f'{self.name} {self.side}'),
        ]
        
    @classmethod
    def get_products(cls, file: Path):
        df = read_products_csv(file)
        return [cls(**d) for d in row_to_dict(df)]
    
    def generate_image(self, path: Path):
        
    
    