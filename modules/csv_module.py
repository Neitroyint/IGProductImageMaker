from pathlib import Path
from pandas import DataFrame, read_csv

def read_products_csv(file: Path) -> DataFrame:
    df = read_csv(str(file))
    return df

def row_to_dict(df: DataFrame) -> list:
    data_list: list = []
    for _, row in df.iterrows():
        data_list.append(
            {
                'code': row['Code'],
                'maker': row['Maker'],
                'brand': row['Brand'],
                'name': row['Name'],
                'buy_price': row['Buy Price'],
                'sell_price': row['Sell Price'],
                'side': row['Side'],
                'created': row['Created'],
            }
        )
    return data_list