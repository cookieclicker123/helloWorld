import yfinance as yf
import plotly.express as px

# Replace these stock symbols with the ones you want to compare
stockSymbol1 = 'AAPL'
stockSymbol2 = 'MSFT'

# Fetch historical data from Yahoo Finance for both stocks
stock_data1 = yf.download(stockSymbol1, start='2020-01-01', end='2022-01-01')
stock_data2 = yf.download(stockSymbol2, start='2020-01-01', end='2022-01-01')

# Create a line chart comparing the closing prices of the two stocks
fig = px.line(stock_data1, x=stock_data1.index, y='Close', title=f'{stockSymbol1} vs {stockSymbol2} Stock Prices Over Time')
fig.add_trace(px.line(stock_data2, x=stock_data2.index, y='Close').data[0])  # Add the second stock data

# Customize the layout
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Stock Price (USD)',
    legend_title='Stock Symbol',
)

# Show the interactive chart
fig.show()
import plotly.graph_objects as go

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=stock_data1.index,
                open=stock_data1['Open'],
                high=stock_data1['High'],
                low=stock_data1['Low'],
                close=stock_data1['Close'])])

# Customize the layout
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Stock Price (USD)',
    title=f'{stockSymbol1} Candlestick Chart'
)

# Show the candlestick chart
fig.show()