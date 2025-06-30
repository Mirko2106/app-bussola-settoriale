import streamlit as st

def show_how_it_works():
    st.title("How it Works?")
    
    st.markdown("""
    This application provides a clear and interactive overview of the **relative strength of sector ETFs** compared to the overall market (**S&P 500**), helping users identify which sectors are gaining or losing momentum.
    """)

    st.image("assets/fibonacci.png", use_container_width=True, caption="")

    st.markdown("## 📊 Dashboard")

    st.markdown("""
    The **Dashboard** section allows you to analyze each GICS sector ETF (e.g., XLK, XLF, XLE) relative to the benchmark index **SPY**.

    First, you will find a candlestick chart of the **S&P 500 (SPY)**.
    
    Then, for each selected ETF, you'll find:
   
    - A candlestick chart of the selected **sector ETF**.
    - A candlestick chart showing the **relative strength** of the ETF vs SPY (**ETF/SPY**).
    - A section with **technical indicators**: *RSI*, *dual EMA*, and *MACD* applied to the ETF/SPY ratio.

    These tools help detect early signs of **sector rotation** and confirm technical **momentum signals**.
    """)

    st.markdown("## 🔀 Discretionary vs Staples")

    st.markdown("""
    This section focuses on the **XLY/XLP ratio**, which compares two key consumer sector ETFs:
    - **XLY**: Consumer Discretionary – cyclical, growth-oriented companies.
    - **XLP**: Consumer Staples – defensive, non-cyclical companies.

    The ratio is widely used as a **risk-on/risk-off sentiment indicator**:
    - A rising ratio implies **confidence in economic growth**.
    - A falling ratio reflects a **defensive market stance**.

    Like the dashboard, this section provides a relative candlestick chart (XLY/XLP) and technical indicators to assess the macroeconomic sentiment.
        """)
    st.markdown("---")
    st.caption("© 2025 – Intermarket Analysis App")