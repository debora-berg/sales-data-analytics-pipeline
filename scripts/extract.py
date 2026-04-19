import pandas as pd

def extract():
    df = pd.read_csv('../data/raw/sales.csv', encoding='latin1')
    print('Dados carregados com sucesso')
    return df

if __name__ == '__main__':
    df = extract()
    print(df.head())
