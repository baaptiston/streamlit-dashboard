import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Titre de l'application
st.title("Tableau de Bord Boursier 📈")

# Sélection de l'action par l'utilisateur
ticker = st.text_input("Entrez un ticker (ex: AAPL, TSLA, MSFT) :", "AAPL")

# Récupération des données
data_ticker = yf.ticker
df = data.history(period="6mo")

# Affichage des prix
st.subheader(f"Cours de {ticker} sur 6 mois")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name="Prix de clôture"))
st.plotly_chart(fig)

# Affichage des indicateurs (ex: Moyenne Mobile 50 jours)
st.subheader("Indicateurs techniques")
df["SMA50"] = df["Close"].rolling(window=50).mean()
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name="Prix de clôture"))
fig2.add_trace(go.Scatter(x=df.index, y=df['SMA50'], mode='lines', name="Moyenne mobile 50j", line=dict(dash='dot')))
st.plotly_chart(fig2)
