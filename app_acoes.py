import streamlit as st    
from datetime import timedelta
import plotly.express as px
from dados_acoes import carregar_acoes, carregar_dados

def app_acoes():
    st.subheader('Esse é um App de ações que mostra uma performace geral das ações selecionadas')
    st.subheader("Performace Dos Ativos")

    acoes = carregar_acoes()
    dados = carregar_dados(acoes)

    # FILTRO DE SELEÇÃO
    lista_selecao = st.multiselect("Escolha as ações para visualizar", dados.columns)
    if lista_selecao:
        dados = dados[lista_selecao]
        if len(lista_selecao) == 1:
            acao_unica = lista_selecao[0]
            dados = dados.rename(columns={acao_unica: 'Close'})

    # FILTRO DE DATAS
    data_inicial = dados.index.min().to_pydatetime()
    data_final = dados.index.max().to_pydatetime()
    intervalo_data = st.slider('SELECIONE O PERÍODO',
                                        min_value=data_inicial,
                                        max_value=data_final,
                                            value=(data_inicial, data_final),
                                            step=timedelta(days=1))

    dados = dados.loc[intervalo_data[0]:intervalo_data[1]] # APLICANDO O FILTRO DE DATAS

    # GRÁFICO
    fig = px.line(dados)
    fig.update_layout(
                    xaxis=dict(
                    title='Data',
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')))

    st.plotly_chart(fig, use_container_width=True)

    # PERFORMACE DOS ATIVOS
    if len(lista_selecao) == 0:
        lista_selecao = list(dados.columns)
    elif len(lista_selecao) == 1:
        dados = dados.rename(columns={'Close': acao_unica})     

    carteira = [1000 for acao in lista_selecao]
    total_inicial_carteira =  sum(carteira)

    texto_performace_ativos = ''
    for indice, ativo in enumerate(lista_selecao):
        performace_ativo = dados[ativo].iloc[-1] / dados[ativo].iloc[0] - 1
        performace_ativo = float(performace_ativo)
    
        carteira[indice] = carteira[indice] * (1 + performace_ativo)
    
        # MUDANDO AS CORES DOS ATIVOS
        if performace_ativo > 0:
            texto_performace_ativos = texto_performace_ativos + f'  \n{ativo}:  :green[{performace_ativo: .1%}]'
        elif performace_ativo < 0:
            texto_performace_ativos = texto_performace_ativos + f'  \n{ativo}:  :red[{performace_ativo: .1%}]'
        else:
            texto_performace_ativos = texto_performace_ativos + f'  \n{ativo}:  {performace_ativo: .1%}'

    total_final_carteira = sum(carteira)
    performace_carteira = total_final_carteira / total_inicial_carteira -1 

    if performace_carteira > 0:
        texto_performace_carteira =  f'PERFORMACE DA CARTEIRA É DE:  :green[{performace_carteira: .1%}]'
    elif performace_carteira < 0:
        texto_performace_carteira =  f'PERFORMACE DA CARTEIRA É DE:  :red[{performace_carteira: .1%}]'
    else:
        texto_performace_carteira =  f'PERFORMACE DA CARTEIRA É DE: {performace_carteira: .1%}'

    st.subheader("ESSA É A PERFORMACE DE CADA ATIVO SELECIONADO: \n" + texto_performace_ativos + '  \n' + texto_performace_carteira)
    st.subheader('Tabela com os ativos selecionados.')
    st.dataframe(dados)