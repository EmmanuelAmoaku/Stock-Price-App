import yfinance as yf
import pandas as pd
import streamlit as st


st.write("""

	# Stock Price App

	##### Shown are the stock **closing price** and **volume** of GOOGLE!


	""")


# Defining the ticker symbol
tickerSymbol = 'GOOGL'


# Obtain data on this ticker symbol
tickerData = yf.Ticker(tickerSymbol)

# Obtain real time prices for this ticker
tickerDf = tickerData.history(period='1y', start='2021-1-01', end='2021-12-31')
# OPEN    HIGH    LOW    CLOSE    VOLUME    DIVIDENDS    STOCK    SPLITS


st.write("""
## Closing Price
	""")
#Plotting a line chart of the closing price
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
	""")
#Plotting a line chart of the volume price
st.line_chart(tickerDf.Volume)