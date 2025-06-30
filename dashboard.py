import streamlit as st
from src.data_manager import get_etf_data, get_benchmark_data, get_relative_candles
from src.plotter import (
    create_candlestick_chart,
    plot_rsi,
    plot_ema,
    plot_macd
)
from src.indicators import calculate_rsi, calculate_ema, calculate_macd


def show_dashboard():


    # Layout iniziale
    st.title("Relative Strength Dashboard")
    st.markdown("Sector ETF analysis relative to the S&P 500 ETF (SPY).")

    # Mappa settori
    etf_sectors = {
        "XLC": "Communication Services",
        "XLY": "Consumer Discretionary",
        "XLP": "Consumer Staples",
        "XLE": "Energy",
        "XLF": "Financials",
        "XLV": "Health Care",
        "XLI": "Industrials",
        "XLB": "Materials",
        "XLRE": "Real Estate",
        "XLK": "Information Technology",
        "XLU": "Utilities"
    }

    # === GRAFICO 1: SPY ===
    df_spy = get_benchmark_data()
    st.subheader("S&P 500 – Benchmark")
    st.plotly_chart(create_candlestick_chart(df_spy, title="SPY – S&P 500"), use_container_width=True)


    # Selezione ETF
    etf_list = [f"{ticker} – {name}" for ticker, name in etf_sectors.items()]
    selected_label = st.selectbox("Choose a sector ETF", options=etf_list)
    selected_ticker = selected_label.split(" – ")[0]
    sector_name = etf_sectors[selected_ticker]

    # === GRAFICO 2: ETF ===
    df_etf = get_etf_data(selected_ticker)
    st.subheader(f"{selected_ticker} – {sector_name}")
    st.plotly_chart(create_candlestick_chart(df_etf, title=f"{selected_ticker} – {sector_name}"), use_container_width=True)

    # === GRAFICO 3: ETF/SPY ===
    df_relative = get_relative_candles(df_etf, df_spy)
    st.subheader(f"⚖️ Relative Strenght: {selected_ticker}/SPY")
    st.plotly_chart(create_candlestick_chart(df_relative, title=f"{selected_ticker}/SPY – Relative Strenght"), use_container_width=True)


    # ============================
    # 📐 Technical Indicators on ETF/SPY
    # ============================

    st.markdown("## 📐 Technical Indicators")

    col1, col2, col3 = st.columns(3)
    with col1:
        rsi_period = st.number_input("RSI period", min_value=2, max_value=100, value=14, step=1)
    with col2:
        ema_short = st.number_input("EMA short", min_value=2, max_value=100, value=12, step=1)
    with col3:
        ema_long = st.number_input("EMA long", min_value=ema_short + 1, max_value=200, value=26, step=1)

    macd_fast = ema_short
    macd_slow = ema_long
    macd_signal = st.number_input("MACD signal", min_value=2, max_value=50, value=9, step=1)

    # RSI
    rsi_series = calculate_rsi(df_relative, period=rsi_period)
    fig_rsi = plot_rsi(df_relative.index, rsi_series)
    st.plotly_chart(fig_rsi, use_container_width=True)

    # Doppia EMA
    ema_fast_series = calculate_ema(df_relative, span=ema_short)
    ema_slow_series = calculate_ema(df_relative, span=ema_long)
    fig_ema = plot_ema(df_relative.index, df_relative["Close"], ema_fast_series, ema_slow_series)
    st.plotly_chart(fig_ema, use_container_width=True)

    # MACD
    macd_line, signal_line, histogram = calculate_macd(df_relative, macd_fast, macd_slow, macd_signal)
    fig_macd = plot_macd(df_relative.index, macd_line, signal_line, histogram)
    st.plotly_chart(fig_macd, use_container_width=True)

    st.markdown("---")
    st.caption("© 2025 – Intermarket Analysis App")