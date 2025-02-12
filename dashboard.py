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
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days = 365)
data_ticker = yf.download(ticker, start = start_date, end = end_date)
close_prices = pd.DataFrame(
  data_ticker(data_ticker.index, data_ticker.Close),
  columns = ['x', 'y'])

# Premier graphique : affichage des données historiques du ticker
st.subheader('Données historiques du titre')
st.write(data_ticker)

# Deuxième graphique : évolution des prix de clôture
st.subheader('Evolution des prix de clôture sur 1 an')
st.line_chart(close_prices)
