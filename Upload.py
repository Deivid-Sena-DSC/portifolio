import plotly.express as px
import streamlit as st   
import pandas as pd
from graficos import graf_barra_agrupada


def upload():
    arquivo_upload = st.file_uploader('Arraste um arquivo')
    with st.spinner('CARREGANDO...'):    
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
                    if len(lista_colunas_data) > 0:
                        filtro_data = st.selectbox('LISTA DE DATAS', options=lista_colunas_data)
                        filtro_opcoes_data = st.multiselect('OPÇÕES DE DATAS', df[filtro_data].unique())
                        df = df[df[filtro_data].isin(filtro_opcoes_data)]
                    filtro_str = st.selectbox('LISTA DE COLUNAS', options=lista_colunas_str)
                    filtro_opcoes_colunas = st.multiselect('OPÇÕES DA COLUNA ESCOLHIDA', df[filtro_str].unique(); df[filtro_str][0])
                    df = df[df[filtro_str].isin(filtro_opcoes_colunas)]
                    filtro_int_float = st.multiselect('LISTA DE COLUNAS NÚMERICAS', lista_colunas_int_float, lista_colunas_int_float[0])
                    with st.spinner('CARREGANDO...'):
                        lista_1 = filtro_int_float
                        lista_1.insert(0, filtro_str)
                        df1 = df[lista_1]
                        st.dataframe(df1)
                        with st.expander('GRÁFICO DE BARRA-SOMA   CLICK PARA EXPANDIR',expanded=False):
                            df2 = df1.groupby(filtro_str)[list(filtro_int_float[1:])].sum()
                            graf2 = px.bar(df2, x=df2.index, y=filtro_int_float[1:], barmode='group')
                            st.plotly_chart(graf2)
                            graf_2 = px.bar(df2, y=df2.index, x=filtro_int_float[1:], barmode='group', orientation='h')
                            st.plotly_chart(graf_2)
                        with st.expander('GRÁFICO DE BARRA-MÉDIA   CLICK PARA EXPANDIR',expanded=False):
                            df3 = df1.groupby(filtro_str)[list(filtro_int_float[1:])].mean()
                            graf3 = px.bar(df3, x=df3.index, y=filtro_int_float[1:], barmode='group')
                            st.plotly_chart(graf3)
                            graf_3 = px.bar(df3, y=df3.index, x=filtro_int_float[1:], barmode='group', orientation='h')
                            st.plotly_chart(graf_3)
                        with st.expander('GRÁFICO DE BARRA-MÁXIMO   CLICK PARA EXPANDIR',expanded=False):
                            df4 = df1.groupby(filtro_str)[list(filtro_int_float[1:])].max()
                            graf4 = px.bar(df4, x=df4.index, y=filtro_int_float[1:], barmode='group')
                            st.plotly_chart(graf4)
                            graf_4 = px.bar(df4, y=df4.index, x=filtro_int_float[1:], barmode='group', orientation='h')
                            st.plotly_chart(graf_4)
                        with st.expander('GRÁFICO DE BARRA-MÍNIMO   CLICK PARA EXPANDIR',expanded=False):
                            df5 = df1.groupby(filtro_str)[list(filtro_int_float[1:])].min()
                            graf5 = px.bar(df5, x=df5.index, y=filtro_int_float[1:], barmode='group')
                            st.plotly_chart(graf5)
                            graf_5 = px.bar(df5, y=df5.index, x=filtro_int_float[1:], barmode='group', orientation='h')
                            st.plotly_chart(graf_5)

                        
                else:
                    st.write('Seu arquivo não tem um número valido de colunas númericas ou de texto')
            