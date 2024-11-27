import streamlit as st
import pandas as pd 
from graficos import graf_barra, graf_barra_linha, graf_barra_agrupada, graf_barra_agrupada2, graf_barra_count, graf_funil, graf_funil_agrupada, graf_line, graf_line_agrupada, graf_pie, graf_pie2, graf_mapa

# Funções para diferentes páginas
@st.cache_data
def home_page():
    st.header("Toda análise de dados começa com uma pergunta que o dados podem respoder.")
    st.header("Me de a chance de usar os dados para responder a sua!")
    st.write('')
    st.subheader("Olá me chamo Deivid S.C. Caldas, obrigado por acessar meu portifólio.")
    st.subheader("Click no icone de '>' no canto superior esquerdo da tela para abrir a barra lateral e rolar para as outras páginas.")

@st.cache_data
def page1():
 
    st.subheader("Viação Grajaú SA.")
    with st.expander("Click para expandir", expanded=False):
         #st.image(r"imagens\viacaograjau.png")
         st.write("Data de início: 04/2022")
         st.write("Data de saída: 06/2024")
         st.write("Descrição do cargo: Controle de saída de frota, rastreamento de frota, assistência aos motoristas, cobradores, fiscais entre outros. Preenchimento de planilhas, operar o sistema SIM da SPTRANS, operar sistemas de telemetria Exemplo NOXXON SAT entre outras, informar mecânicos sobre coletivos que necessitam de concerto na via, acompanhar e fazer abertura de fichas de manutenção, relatórios sobre o cumprimento de frota, preenchimento de relatórios e ocorrências em planilhas Excel.")

    st.subheader("CNB Serviços de Inventário.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/cnb.png")
         st.write("Data de início: 09/2020")
         st.write("Data de saída: 04/2022")
         st.write("Separação e organização da área de venda para realizar contagem utilizando HUB, contagem de estoque, hortifruti, congelados e resfriados, contagem de todos os tipos de produtos no mercado atacadão.")

    st.subheader("Socicam Administração Projetos e Representações LTDA.")
    with st.expander("Click para expandir", expanded=False):
         st.image(r"imagens/socicam.png")
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


def page3():
    st.subheader('Aqui eu demostro um pouco do que eu sei fazer')
    tab1, tab2, tab3, tab4 = st.tabs(['Dashboard de serviço de assinatura', 'Dashboard de vendas', 'Correlação de Pearson', 'Árvore de decisão'])

    with tab1:
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agoto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        novos_usuarios = [100, 80, 110, 140, 150, 160, 170, 120, 110, 150, 200, 140]
        usuarios_ativos_diarios = [1000, 750, 900, 1300, 1400, 1500, 1200, 1200, 1500, 1900, 2000, 1800]
        receita_mensal = [10000, 8500, 9800, 10000, 11000, 12000, 10000, 10500, 13000, 13000, 20000, 17000]
        tickets_suporte_abertos = [110, 75, 100, 140, 170, 160, 100, 130, 190, 200, 210, 140]
        tickets_suporte_fechados = [100, 85, 100, 120, 130, 150, 140, 110, 130, 120, 150, 200]
        selecao_meses = st.selectbox('', ['Receita Mensal', 'Total de novos usuários mensal', 'Média de usuários ativos diários', 'Tickets'])
        
        if selecao_meses == 'Receita Mensal':
            st.write(f'Total de receita R$: {sum(receita_mensal):,.2f}')
            st.plotly_chart(graf_barra(meses, receita_mensal, meses, ''), use_container_width=True)
            st.plotly_chart(graf_line(meses, receita_mensal, ''), use_container_width=True)
            st.plotly_chart(graf_pie(meses, receita_mensal, meses, ''), use_container_width=True)
        if selecao_meses == 'Total de novos usuários mensal':
            st.write(f'Total de novos usuários {sum(novos_usuarios):.0f}')
            st.plotly_chart(graf_barra(meses, novos_usuarios, meses, ''), use_container_width=True)
            st.plotly_chart(graf_line(meses, novos_usuarios, ''), use_container_width=True)
            st.plotly_chart(graf_pie(meses, novos_usuarios, meses, ''), use_container_width=True)
        if selecao_meses == 'Média de usuários ativos diários':
            st.plotly_chart(graf_barra(meses, usuarios_ativos_diarios, meses, ''), use_container_width=True)
            st.plotly_chart(graf_line(meses, usuarios_ativos_diarios, ''), use_container_width=True)
            st.plotly_chart(graf_funil(meses, usuarios_ativos_diarios), use_container_width=True)
        if selecao_meses == 'Tickets':
            st.write(f'Total de Tickets Abertos {sum(tickets_suporte_abertos)} Total de Tickets Fechados {sum(tickets_suporte_fechados)}')
            st.plotly_chart(graf_barra_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados', 'Tickets Abertos X Fechados'), use_container_width=True)
            st.plotly_chart(graf_line_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados', 'Tickets Abertos X Fechados'), use_container_width=True)
            st.plotly_chart(graf_funil_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados'), use_container_width=True)
                   
    with tab2:
        def df_vendas():
            df = pd.read_excel(r'Excel/Vendas Consolidado.xlsx')

            df['Valor Unitario'] = df['Valor Unitario'].astype('float')
            df['Faturamento'] = df['Faturamento'].astype('float')
            df['Lucro'] = df['Lucro'].astype('float')

            df.drop_duplicates()

            df.drop(columns='Unnamed: 0', axis=0, inplace=True)

            return df

        df = df_vendas()

        st.subheader('Mude os filtros abaixo para mudar os Dashboards')

        filtro_ano = st.multiselect('Anos', df['Ano'].unique(), df['Ano'].unique()) # 1º FILTRO ANO
        df_ano = df[df['Ano'].isin(filtro_ano)] # APLICANDO O FILTRO DE ANO

        filtro_mes = st.multiselect('Meses', df_ano['Mês'].unique(), df_ano['Mês'].unique()) # 2º FILTRO MÊS
        df_mes = df_ano[df_ano['Mês'].isin(filtro_mes)] # APLICANDO O FILTRO DE MÊS

        filtro_dia = st.multiselect('Dias da semana', df_mes['Dia da semana'].unique(), df_mes['Dia da semana'].unique()) # 3º FILTRO DIA
        df_dia = df_mes[df_mes['Dia da semana'].isin(filtro_dia)] # APLICANDO O FILTRO DE DIA

        filtro_loja = st.multiselect('Lojas', df_dia['Loja'].unique(), df_dia['Loja'].unique()) # 5º FILTRO LOJA
        df_loja = df_dia[df_dia['Loja'].isin(filtro_loja)] # APLICANDO O FILTRO DE LOJA

        filtro_estado = st.multiselect('Estados', df_loja['Estado'].unique(), df_loja['Estado'].unique()) # 4º FILTRO ESTADO
        df_estado = df_loja[df_dia['Estado'].isin(filtro_estado)] # APLICANDO O FILTRO DE ESTADO
            
        filtro_produto = st.multiselect('Produtos', df_estado['Produto'].unique(), df_estado['Produto'].unique()) # 6º FILTRO PRODUTO
        df_produto = df_estado[df_estado['Produto'].isin(filtro_produto)] # APLICANDO O FILTRO DE ESTADO

        faturamento = df_produto['Faturamento'].sum()
        lucro = df_produto['Lucro'].sum()
        quantidade_prod = df_produto['Produto'].count()
        dicionario = {'Faturamento Total': faturamento, 'Lucro Total': lucro, 'Quantidade de produtos vendidos': quantidade_prod}
        st.table(dicionario)

        st.write('Click na legenda a direita para retirar as Barras ou as Linhas')    
        st.plotly_chart(graf_barra_linha(df_produto, 'Mês', 'Faturamento', 'Faturamento Mensal R$'), use_container_width=True)
        st.plotly_chart(graf_barra_linha(df_produto, 'Mês', 'Lucro', 'Lucro Mensal R$'), use_container_width=True)
        st.plotly_chart(graf_barra_linha(df_produto, 'Dia da semana', 'Faturamento', 'Faturamento por dia da semana R$'), use_container_width=True)
        st.plotly_chart(graf_barra_linha(df_produto, 'Dia da semana', 'Lucro', 'Lucro por dia da semana R$'), use_container_width=True)
        st.plotly_chart(graf_barra_agrupada2(df_produto, 'Mês', 'Faturamento', 'Loja', 'Comparação de Faturamento Mensal por Loja'), use_container_width=True)
        st.plotly_chart(graf_barra_agrupada2(df_produto, 'Mês', 'Faturamento', 'Produto', 'Comparação de Faturamento Mensal por Produto'), use_container_width=True)
        st.plotly_chart(graf_barra_count(df_produto, 'Mês', 'Produto', 'Quantidade de Produtos Vendidos por Mês'), use_container_width=True)
        st.plotly_chart(graf_barra_count(df_produto, 'Loja', 'Produto', 'Quantidade de Produtos Vendidos por Loja'), use_container_width=True)
        coluna1 , coluna2 = st.columns(2)
        coluna1.plotly_chart(graf_pie2(df_produto, 'Loja', 'Faturamento', 'Faturamento por Loja %'), use_container_width=True)
        coluna2.plotly_chart(graf_pie2(df_produto, 'Produto', 'Faturamento', 'Faturamento por Produto %'), use_container_width=True)
        st.plotly_chart(graf_mapa(df_produto, 'Latitude', 'Longitude', 'Faturamento', 'Estado'))
        coluna3 , coluna4 = st.columns(2)
        coluna3.plotly_chart(graf_pie2(df_produto, 'Loja', 'Lucro', 'Lucro por Loja %'), use_container_width=True)
        coluna4.plotly_chart(graf_pie2(df_produto, 'Produto', 'Lucro', 'Lucro por Produto %'), use_container_width=True)          