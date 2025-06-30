# src/plotter.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_candlestick_chart(df, title=""):
    # Se c'è Volume, mostra anche il grafico barra sotto
    has_volume = "Volume" in df.columns

    fig = make_subplots(
        rows=2 if has_volume else 1, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_heights=[0.7, 0.3] if has_volume else [1],
        specs=[[{"type": "candlestick"}]] + ([[{"type": "bar"}]] if has_volume else [])
    )

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"], high=df["High"],
        low=df["Low"], close=df["Close"],
        name="Candlestick"
    ), row=1, col=1)

    if has_volume:
        fig.add_trace(go.Bar(
            x=df.index,
            y=df["Volume"],
            name="Volume",
            marker_color="lightblue",
            opacity=0.4
        ), row=2, col=1)

    fig.update_layout(
        title=title,
        height=700,
        xaxis_rangeslider_visible=False,
        template="plotly_white"
    )

    return fig



def plot_rsi(dates, rsi_series):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=rsi_series, mode='lines', name='RSI'))
    fig.update_layout(
        title="RSI",
        height=300,
        template="plotly_white",
        yaxis=dict(range=[0, 100]),
        shapes=[
            {"type": "line", "x0": dates.min(), "x1": dates.max(), "y0": 70, "y1": 70,
             "line": {"color": "red", "dash": "dash"}},
            {"type": "line", "x0": dates.min(), "x1": dates.max(), "y0": 30, "y1": 30,
             "line": {"color": "green", "dash": "dash"}}
        ]
    )
    return fig



def plot_ema(dates, close, ema1, ema2):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=close, name="Close", line=dict(color="gray")))
    fig.add_trace(go.Scatter(x=dates, y=ema1, name="EMA Fast"))
    fig.add_trace(go.Scatter(x=dates, y=ema2, name="EMA Slow"))
    fig.update_layout(title="Exponential Moving Averages", height=300, template="plotly_white")
    return fig



def plot_macd(dates, macd, signal, hist):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=macd, name="MACD", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=dates, y=signal, name="Signal", line=dict(color="orange")))
    fig.add_trace(go.Bar(x=dates, y=hist, name="Histogram", marker_color="gray"))
    fig.update_layout(title="MACD", height=300, template="plotly_white")
    return fig

