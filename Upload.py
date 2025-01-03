import plotly.express as px
import streamlit as st   
import pandas as pd 


def upload():
    arquivo_upload = st.file_uploader('Arraste um arquivo')
    if arquivo_upload is not None:
        if arquivo_upload.name.endswith('.xlsx') or arquivo_upload.name.endswith('.xls'):
            df = pd.read_excel(arquivo_upload)
            lista_colunas_str = []
            lista_colunas_int_float = []
            lista_colunas_data = []
            for coluna in df.columns:
                if coluna == "Ano" or coluna == "ano" or coluna == 'Anos' or coluna == "anos":
                    df[coluna] = df[coluna].astype(str)
                if coluna == "Mês" or coluna == "Mes" or coluna == "mês" or coluna == "mes" or coluna == "Meses" or coluna == "meses":
                    df[coluna] = df[coluna].astype(str)
                if df[coluna].dtype == 'object':
                    lista_colunas_str.append(coluna)
                elif df[coluna].dtype == 'int64' or df[coluna].dtype == 'float64':
                    lista_colunas_int_float.append(coluna)
                elif df[coluna].dtype == 'datetime64[ns]':
                    lista_colunas_data.append(coluna)
            if len(lista_colunas_str) > 0 and len(lista_colunas_int_float) > 0:
                filtro_str = st.selectbox('LISTA DE COLUNAS', options=lista_colunas_str)
                filtro_opcoes_colunas = st.multiselect('OPÇÕES DA COLUNA ESCOLHIDA', df[filtro_str].unique(), df[filtro_str].unique())
                df = df[df[filtro_str].isin(filtro_opcoes_colunas)]
                filtro_int_float = st.multiselect('LISTA DE COLUNAS NÚMERICAS', lista_colunas_int_float, lista_colunas_int_float)
                lista_1 = filtro_int_float
                lista_1.insert(0, filtro_str)
                df1 = df[lista_1]
                st.dataframe(df1)
                graf = px.bar(df1, x=filtro_str, y=filtro_int_float, barmode='group')
                st.plotly_chart(graf)	

                pass
            else:
                st.write('Seu arquivo não tem um número valido de colunas númericas ou de texto')
            