import os
import requests
import pandas as pd
from sqlalchemy import create_engine

API_URL = "https://api.collectapi.com/economy/goldPrice"


def fetch_gold_prices():
    """Fetch gold prices from the CollectAPI gold price endpoint."""
    api_key = os.getenv("COLLECTAPI_KEY")

    if not api_key:
        raise ValueError(
            "COLLECTAPI_KEY is not set. Add your API key as an environment variable."
        )

    headers = {
        "content-type": "application/json",
        "authorization": f"apikey {api_key}",
    }

    response = requests.get(API_URL, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "result" not in data:
        raise ValueError("The API response does not contain a 'result' field.")

    return pd.DataFrame(data["result"])


def save_to_postgres(df):
    """Save the gold price DataFrame to PostgreSQL."""
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is not set. Add your PostgreSQL connection string "
            "as an environment variable."
        )

    engine = create_engine(database_url)

    df.to_sql(
        "gold_prices",
        engine,
        if_exists="replace",
        index=False,
        schema="gold",
    )

    print(f"Saved {len(df)} records to gold.gold_prices.")


def main():
    """Run the gold price ETL pipeline."""
    print("Fetching gold prices...")
    df = fetch_gold_prices()

    print(f"Fetched {len(df)} records.")
    print(df.head())

    save_to_postgres(df)
    print("Gold price ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
