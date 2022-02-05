import pandas as pd
import os

PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(PATH, 'templates/payment.ods')
def create_table(input_file):
    df = pd.read_excel(input_file, 'Sheet1')
    print(df)

create_table(INPUT_FILE)


