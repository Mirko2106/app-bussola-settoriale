#src/data_manager.py
import pandas as pd
import os
import streamlit as st

DATA_DIR = "data"
ETF_DIR = os.path.join(DATA_DIR, "etf")
BENCHMARK_DIR = os.path.join(DATA_DIR, "benchmark")

@st.cache_data
def get_etf_data(ticker: str) -> pd.DataFrame:
    """Carica i dati di un ETF dal file CSV, con caching."""
    file_path = os.path.join(ETF_DIR, f"{ticker}.csv")
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return df

@st.cache_data
def get_benchmark_data() -> pd.DataFrame:
    """Carica i dati di SPY (benchmark) dal file CSV, con caching."""
    file_path = os.path.join(BENCHMARK_DIR, "SPY.csv")
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return df

@st.cache_data
def get_relative_candles(etf_df: pd.DataFrame, spy_df: pd.DataFrame) -> pd.DataFrame:
    """Calcola il grafico candlestick della forza relativa (ETF / SPY)."""
    df = pd.DataFrame(index=etf_df.index)
    df["Open"] = etf_df["Open"] / spy_df["Open"]
    df["High"] = etf_df["High"] / spy_df["High"]
    df["Low"] = etf_df["Low"] / spy_df["Low"]
    df["Close"] = etf_df["Close"] / spy_df["Close"]
    return df
