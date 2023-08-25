import pandas as pd
from api.models import Bank


def load_data_from_excel(file_path):
    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        item = Bank(name=row['Name'], description=row['Description'])
        item.save()


if __name__ == '__main__':
    excel_file_path = '../../68774.xlsx'
    load_data_from_excel(excel_file_path)
