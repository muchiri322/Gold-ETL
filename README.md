# Gold-ETL

📄 Notebook Profile: Gold Price API Data Extraction
🧾 Overview
This notebook is designed to:

Connect to a public API providing gold price data.

Fetch and parse the data in JSON format.

Prepare it for further use, such as storage in a database or data analysis using Python tools like Pandas and SQLAlchemy.

🔧 Key Components
Library Imports:

python
Copy
Edit
import requests
import pandas as pd
from sqlalchemy import create_engine
These are standard libraries used for HTTP requests (requests), data manipulation (pandas), and database interaction (sqlalchemy).

API Request:

python
Copy
Edit
url = 'https://api.collectapi.com/economy/goldPrice'
headers = {
    'content-type': "application/json",
    'authorization': "apikey YOUR_API_KEY"
}
response = requests.get(url, headers=headers)
Connects to the CollectAPI economy endpoint for goldPrice data.

Uses an API key (make sure to keep it secure in practice).

Returns a response with status 200, indicating a successful connection.

JSON Parsing:

python
Copy
Edit
data = response.json()
gold = data['result']
Parses the JSON response.

Extracts the "result" field, which likely contains the gold price data.

📦 Next Steps Likely Intended
Based on the imports and setup, the notebook might continue with:

Converting gold data into a Pandas DataFrame.

Performing cleaning or transformation.

Saving the data into a SQL database using SQLAlchemy.
