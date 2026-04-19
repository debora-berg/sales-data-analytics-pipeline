import pandas as pd

def transform(df):
    df = df.dropna()

    df['Order Date'] = pd.to_datetime(df['Order Date'])

    if 'Sales' in df.columns:
        df['Revenue'] = df['Sales']

    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

    print('Tranformação concluída')
    return df