import streamlit as st
import pandas as pd 
from graficos import graf_barra, graf_barra_linha, graf_barra_agrupada, graf_barra_agrupada2, graf_barra_count, graf_funil, graf_funil_agrupada, graf_line, graf_line_agrupada, graf_pie, graf_pie2, graf_mapa

# Funções para diferentes páginas
@st.cache_data
def home_page():
    st.header("Toda análise de dados começa com uma pergunta que o dados podem responder.")
    st.header("Me de a chance de usar os dados para responder a sua!")
    st.write('')
    st.subheader("Olá me chamo Deivid S.C. Caldas, obrigado por acessar meu portifólio.")
    st.subheader("Click no icone de '>' no canto superior esquerdo da tela para abrir a barra lateral e rolar para as outras páginas.")

@st.cache_data
def page1():
 
    st.subheader("Viação Grajaú SA.")
    with st.expander("Click para expandir", expanded=False):
         #st.image(r"imagens\viacaograjau.png")
         st.write('Cargo: Assistende de centro de operações da concessionária.')
         st.write("Data de início: 04/2022")
         st.write("Data de saída: 06/2024")
         st.write("Descrição do cargo: Controle de saída de frota, rastreamento de frota, assistência aos motoristas, cobradores, fiscais entre outros. Preenchimento de planilhas, operar o sistema SIM da SPTRANS, operar sistemas de telemetria Exemplo NOXXON SAT entre outras, informar mecânicos sobre coletivos que necessitam de concerto na via, acompanhar e fazer abertura de fichas de manutenção, relatórios sobre o cumprimento de frota, preenchimento de relatórios e ocorrências em planilhas Excel.")

    st.subheader("CNB Serviços de Inventário.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/cnb.png")
         st.write('Cargo: Inventariante.')
         st.write("Data de início: 09/2020")
         st.write("Data de saída: 04/2022")
         st.write("Separação e organização da área de venda para realizar contagem utilizando HUB, contagem de estoque, hortifruti, congelados e resfriados, contagem de todos os tipos de produtos no mercado atacadão.")

    st.subheader("Socicam Administração Projetos e Representações LTDA.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/socicam.png")
         st.write('Cargo: Agente de Terminal Urbano.')
         st.write("Data de início: 02/2015")
         st.write("Data de saída: 07/2019")
         st.write("Auxílio e informações á usuários do terminal, condução e auxílio a usuário PCD, Administração do terminal, elaboração de relatórios diários em livro, envio de e-mails, solicitação e acompanhamento manutenções no terminal, utilização do código Q, monitoramento CFTV, rastreamento de veículos por GPS em sistema integrado.")


@st.cache_data
def page2():
    
    st.subheader("Power BI.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/senai.png")
         st.write("Data de início: 09/2024 até 11/2024 duração 40 horas.")
         st.write("Competências: Dashboard, Relatórios e análises, Microsoft Power Query, Indicadores chave de desempenho KPI's, DAX, modelagem de dados.")
         
    st.subheader("Análise de dados em nuvem  Microsoft DP-900.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/senai.png")
         st.write("Data de início: 09/2024 até 10/2024 duração 40 horas")
         st.write("Competências: Windows Azure, Azure Data Factory, Azure DataLake, Azure Functions, Azure Cosmos DB, Máquina Virtual, Azure Databricks, SQL Azure.")
         
    st.subheader("Python para Data Science.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/senai.png")
         st.write("Data de início: 08/2024 até 09/2024 duração 60 horas")
         st.write("Competências: Análises Descritiva, Diagnóstica, Preditiva, Prescritiva. Python bibliotecas Pandas, Matplotlib, Seaborn, Numpy, Datetime, Aed. Correlação, Modelos quantitativos, Árvore de decisão, Regressão linear, Manipulação e Transformação de Dados, Análise de cluster.")

    st.subheader("Programação em Python")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/senai.png")
         st.write("Data de início: 07/2024 até 08/2024 duração 60 horas")
         st.write(r"Competências: Identificar os requisitos do problema para definição dos recursos a serem utilizados, Elaborar algoritmo da solução do problema, Configurar o ambiente de desenvolvimento em Python, Programar em linguagem Python, Programar jogos 2D em linguagem Python, Validar software por meio de testes")         


