from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import streamlit as st

def app_moedas():
    link = "https://coinmarketcap.com/pt-br/"
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, 'html.parser')
    tabela = site.find('tbody')
    linhas = tabela.find_all('tr')

    moedas = []
    for c in range(0,10):
        logo = linhas[c].find(class_='coin-logo')
        nome = linhas[c].find_all('td') 
        valor = linhas[c].find_all('td')
        percentuais = linhas[c].find_all(string=re.compile('%'))
        up_dow = linhas[c].find_all(class_=re.compile('icon-Caret'))
        for i, u_d in enumerate(up_dow):
            if 'icon-Caret-down' in u_d['class']:
                percentuais[i] = '▼' + percentuais[i]
            else:
                percentuais[i] = '▲' + percentuais[i]
        dicionario = {"Logo": logo['src'], "Nome": nome[2].text, "Valor": valor[3].text, "1h %": percentuais[0], "24h %": percentuais[1], "7d %": percentuais[2]}
        moedas.append(dicionario)
    df = pd.DataFrame(moedas)
    return st.dataframe(df, column_config={"Logo": st.column_config.ImageColumn("Logo", width='small')}, use_container_width=True)