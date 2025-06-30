import streamlit as st
from streamlit_option_menu import option_menu

# Importa le pagine
import dashboard
import discretionary_vs_staples
import how_it_works
import contact

# === 1. AGGIUNGI QUESTO BLOCCO ALL'INIZIO ===
from src.data_loader import DataLoader

# Lista ETF da aggiornare
etf_tickers = [
    "XLC", "XLY", "XLP", "XLE", "XLF", "XLV",
    "XLI", "XLB", "XLRE", "XLK", "XLU", "SPY"  # Include anche SPY
]

API_KEY_EOD = "682f8953cd5977.53197537"

loader = DataLoader(etf_tickers, api_key=API_KEY_EOD)
loader.update_data()


# Config pagina principale
st.set_page_config(page_title="Relative Strength Analyzer", layout="wide")

# Sidebar con menu
with st.sidebar:
    selected = option_menu(
        "Navigazione",
        ["Dashboard", "Discretionary vs Staples", "How it Works", "Contact Me"],
        icons=["bar-chart", "shuffle", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0
    )

# Routing delle pagine
if selected == "Dashboard":
    dashboard.show_dashboard()
elif selected == "Discretionary vs Staples":
    discretionary_vs_staples.show_discretionary_vs_staples()
elif selected == "How it Works":
    how_it_works.show_how_it_works()
elif selected == "Contact Me":
    contact.show_contact()

# Nascondi menu default Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
