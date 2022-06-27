from pathlib import Path
from pandas import DataFrame, read_csv

def read_products_csv(file: Path) -> DataFrame:
    df = read_csv(str(file), dtype={'Code': str})
    return format_data(df)

def format_data(df) -> DataFrame:
    df['Code'] = df['Code'].astype(str)
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
                'car1': row['Car 1'],
                'car2': row['Car 2'],
            }
        )
    return data_list