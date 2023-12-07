import yfinance as yf
import sqlite3
import pandas as pd

df = yf.download("2330.TW", start='2021-12-03', end='2023-12-04')
print(df)

df.to_csv('fileoutput.csv', index=True, sep=',')

conn = sqlite3.connect('stock_database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stockTable (
        Date DATE PRIMARY KEY,
        Open FLOAT NOT NULL,
        High FLOAT NOT NULL,
        Low FLOAT NOT NULL,
        Close FLOAT NOT NULL,
        Volume FLOAT NOT NULL
    )
''')

conn.commit()

df.to_sql('stockTable', conn, if_exists='append', index=True, index_label='Date')

conn.close()
