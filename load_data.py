import os
import sys
import pandas as pd

# Add your Django project's directory to the sys path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Import and configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankifsc.settings')
import django
django.setup()

# Now you can import your models
from api.models import Bank

def load_data_from_excel(file_path):
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        for index, row in data.iterrows():
            item = Bank(bank_name=row['BANK'], ifsc=row['IFSC'], branch=row['BRANCH'], address=row['ADDRESS'], city1=row['CITY1'], city2=row['CITY2'], state=row['STATE'], std_code=row['STD CODE'], phone=row['PHONE'])
            item.save()

if __name__ == '__main__':
    excel_file_path = '68774.xlsx'
    load_data_from_excel(excel_file_path)

