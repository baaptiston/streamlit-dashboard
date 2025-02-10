import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("Tableau de bord interactif des actions 📈")

ticker = st.text_input("Entrez un ticker (ex: AAPL, TSLA, ^GSPC)", "AAPL")

data = yf.download(ticker, period="1y")
data["Returns"] = data["Adj Close"].pct_change()

st.subheader("Données historiques du titre")
st.write(data.tail())

st.subheader("Évolution du prix de clôture")
fig = px.line(data, x=data.index, y="Adj Close", title=f"Prix de clôture de {ticker}")
st.plotly_chart(fig)

st.subheader("Distribution des rendements")
fig2 = px.histogram(data, x="Returns", nbins=50, title=f"Distribution des rendements de {ticker}")
st.plotly_chart(fig2)
