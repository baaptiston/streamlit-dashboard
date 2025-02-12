import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import datetime as dt

# Titre du tableau de bord
st.title('Tableau de bord interactif des actions')

# Texte input pour demander le ticker à analyser
ticker = st.text_input('Entrez un ticker (ex : AAPL, TSLA, ^GSPC, ...)')

# Déclaration des variables
data_ticker = yf.download(ticker, period="1y")
close_prices = data_ticker['Close']

# Premier graphique : affichage des données historiques du ticker
st.subheader('Données historiques du titre')
st.write(data_ticker)

# Deuxième graphique : évolution des prix de clôture
st.subheader('Evolution des prix de clôture sur 1 an')
fig = px.line(data_ticker, x = data_ticker.index, y = data_ticker['Close'], title = f'Prix de clôture de {ticker}')
st.plotly_chart(fig)
