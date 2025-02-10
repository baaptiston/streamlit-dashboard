import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import datetime as dt

st.title("Tableau de bord interactif des actions 📈")

ticker = st.text_input("Entrez un ticker (ex: AAPL, TSLA, ^GSPC)", "AAPL")

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365)

data = yf.download(ticker, start = startDate, end = endDate)
data["Returns"] = data.Close.pct_change()

st.subheader("Données historiques du titre")
st.write(data.tail())

st.subheader("Évolution du prix de clôture")
fig = px.line(data, x=data.index, y="Adj Close", title=f"Prix de clôture de {ticker}")
st.plotly_chart(fig)

st.subheader("Distribution des rendements")
fig2 = px.histogram(data, x="Returns", nbins=50, title=f"Distribution des rendements de {ticker}")
st.plotly_chart(fig2)
