# src/data_loader.py

import os
import requests
import pandas as pd
from datetime import datetime

class DataLoader:
    def __init__(self, tickers, api_key, data_dir="data", start_date="2000-01-01"):
        self.tickers = tickers
        self.api_key = api_key
        self.data_dir = data_dir
        self.start_date = start_date
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.update_flag_path = os.path.join(data_dir, "last_update.txt")
        self.base_url = "https://eodhistoricaldata.com/api/eod"

    def is_data_fresh(self):
        """Controlla se i dati sono stati aggiornati oggi."""
        if not os.path.exists(self.update_flag_path):
            return False
        with open(self.update_flag_path, "r") as f:
            last_update = f.read().strip()
        return last_update == self.today

    def mark_data_as_fresh(self):
        """Segna che i dati sono stati aggiornati oggi."""
        with open(self.update_flag_path, "w") as f:
            f.write(self.today)

    def update_data(self):
        """Scarica e aggiorna i dati per tutti i ticker solo se necessario."""
        if self.is_data_fresh():
            print("✔️  Dati già aggiornati oggi. Nessuna richiesta a EOD.")
            return

        print("🔄 Aggiornamento dati in corso...")
        for ticker in self.tickers:
            self._download_and_append(ticker)

        self.mark_data_as_fresh()
        print("✅ Dati aggiornati e salvati.")

    def _download_and_append(self, ticker):
        """Scarica e aggiorna i dati di un singolo ticker da EOD."""
        subfolder = "benchmark" if ticker == "SPY" else "etf"
        folder_path = os.path.join(self.data_dir, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"{ticker}.csv")

        # Controlla ultima data nel CSV
        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path, index_col="Date", parse_dates=True)
            last_date = df_existing.index[-1].strftime("%Y-%m-%d")
        else:
            df_existing = None
            last_date = self.start_date

        # Richiesta all'API di EOD
        url = f"{self.base_url}/{ticker}.US"
        params = {
            "api_token": self.api_key,
            "from": last_date,
            "to": self.today,
            "period": "d",
            "fmt": "json"
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"❌ Errore nel download di {ticker}: {response.status_code}")
            return

        try:
            data = pd.DataFrame(response.json())
            if data.empty:
                print(f"⚠️ Nessun nuovo dato per {ticker}")
                return

            data['date'] = pd.to_datetime(data['date'])
            data.set_index('date', inplace=True)
            data.sort_index(inplace=True)
            data.rename(columns={
                'open': 'Open',
                'high': 'High',
                'low': 'Low',
                'close': 'Close',
                'adjusted_close': 'Adj Close',
                'volume': 'Volume'
            }, inplace=True)
            data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

            # Append a dati esistenti
            if df_existing is not None:
                data = data[~data.index.isin(df_existing.index)]  # evita duplicati
                df_combined = pd.concat([df_existing, data])
            else:
                df_combined = data

            df_combined.to_csv(file_path, index_label="Date")
            print(f"✅ {ticker} aggiornato ({len(data)} nuove righe)")
        except Exception as e:
            print(f"❌ Errore parsing dati per {ticker}: {e}")
