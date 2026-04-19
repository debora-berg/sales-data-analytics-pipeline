import sqlite3

def load(df):
    conn = sqlite3.connect('../data/processed/sales.db')
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()
    print("Dados salvos no banco SQLite")
