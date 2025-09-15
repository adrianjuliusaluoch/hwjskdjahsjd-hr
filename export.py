# Import Packages
from google.cloud import bigquery
import pandas as pd

# Initialize Client
client = bigquery.Client(project='crypto-stocks-01')

# Define SQL Query to Retrieve Crypto Data
query = """
    SELECT * 
    FROM `crypto-stocks-01.storage.top_cryptocurrency`
    ORDER BY timestamp DESC
"""
crypto = client.query(query).to_dataframe()

# Define SQL Query to Retrieve Stocks Data
query = """
    SELECT * 
    FROM `crypto-stocks-01.storage.top_stocks`
    ORDER BY timestamp DESC
"""
stocks = client.query(query).to_dataframe()

crypto.to_csv("storage/cryptocurrency.csv", index=False, encoding='utf-8')
stocks.to_csv("storage/stocks.csv", index=False, encoding='utf-8')
