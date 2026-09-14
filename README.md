# Gold Price ETL Pipeline

A simple Python ETL pipeline that extracts gold price data from CollectAPI, processes it with Pandas, and loads it into PostgreSQL.

## Architecture

```text
CollectAPI
    |
    v
Python / Requests
    |
    v
Pandas DataFrame
    |
    v
PostgreSQL
gold.gold_prices
```

## Technologies

- Python
- Requests
- Pandas
- SQLAlchemy
- PostgreSQL
- CollectAPI

## Data Fields

The API response used by the project contains fields such as:

- `name`
- `buying`
- `buyingstr`
- `selling`
- `sellingstr`
- `time`
- `date`
- `datetime`
- `rate`

## Project Structure

```text
gold-price-etl/
│
├── gold.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup

### 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv goldenv
goldenv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv goldenv
source goldenv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Do not place API keys or database passwords directly in `gold.py`.

Windows PowerShell:

```powershell
$env:COLLECTAPI_KEY="your_api_key"
$env:DATABASE_URL="postgresql://username:password@host:port/database"
```

Linux/macOS:

```bash
export COLLECTAPI_KEY="your_api_key"
export DATABASE_URL="postgresql://username:password@host:port/database"
```

## Run the Pipeline

```bash
python gold.py
```

The pipeline will:

1. Connect to the CollectAPI gold-price endpoint.
2. Fetch the JSON response.
3. Extract the `result` records.
4. Convert the records into a Pandas DataFrame.
5. Load the data into the PostgreSQL table `gold.gold_prices`.

## PostgreSQL

The script expects the PostgreSQL schema `gold` to exist.

If necessary, create it with:

```sql
CREATE SCHEMA IF NOT EXISTS gold;
```

## Security

Never commit API keys, passwords, database connection strings, `.env` files, or other credentials to GitHub.

If credentials were previously exposed in source code or a notebook, rotate them before using the project publicly.

## License

This project is intended for learning and portfolio purposes.
