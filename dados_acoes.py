import streamlit as st
import pandas as pd   
import yfinance as yf
from datetime import datetime

data_atual = datetime.now().strftime("%Y-%m-%d")

@st.cache_data 
def carregar_dados(empresa):
    texto_tickers = " ".join(empresa)
    acao = yf.Tickers(texto_tickers)
    cotacao_acao = acao.history(period="1d", start="2025-01-01", end=data_atual)
    cotacao_acao = cotacao_acao['Close']
    return cotacao_acao

# FUNÇÃO PARA CARREGAR OS NOMES DOS TICKERS
@st.cache_data
def carregar_acoes():
    base_acoes = pd.read_csv('Excel/IBOV.csv', sep=';')
    tickers = list(base_acoes['Código'])
    tickers = [item + '.SA' for item in tickers]
    return tickers
