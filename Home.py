import streamlit as st
import pandas as pd
from Upload import upload
from app_acoes import app_acoes 
from app_moedas import app_moedas
from graficos import graf_barra, graf_barra_linha, graf_barra_agrupada, graf_barra_agrupada2, graf_barra_count, graf_funil, graf_funil_agrupada, graf_line, graf_line_agrupada, graf_pie, graf_pie2, graf_mapa


# Funções para diferentes páginas
def home_page():
    st.subheader("Olá me chamo Deivid S.C. Caldas, obrigado por acessar meu portifólio.")
    st.subheader("Click no icone de '>' no canto superior esquerdo da tela para abrir a barra lateral e rolar para as outras páginas.")
    st.subheader('COTAÇÃO DE CRIPTO MOEDAS')
    app_moedas()
    st.subheader('Aqui eu demostro um pouco do que eu sei fazer')
    tab1, tab2, tab3, tab4 = st.tabs(['DASHBOARD DE SERVIÇO DE ASSINATURA', 'DASHBOARD DE VENDAS', 'APP DE AÇÕES', 'APP DE DASHBOARDS'])

    with tab1:
        with st.spinner('CARREGANDO...'):
            meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
            novos_usuarios = [100, 80, 110, 140, 150, 160, 170, 120, 110, 150, 200, 140]
            usuarios_ativos_diarios = [1000, 750, 900, 1300, 1400, 1500, 1200, 1200, 1500, 1900, 2000, 1800]
            receita_mensal = [10000, 8500, 9800, 10000, 11000, 12000, 10000, 10500, 13000, 13000, 20000, 17000]
            tickets_suporte_abertos = [110, 75, 100, 140, 170, 160, 100, 130, 190, 200, 210, 140]
            tickets_suporte_fechados = [100, 85, 100, 120, 130, 150, 140, 110, 130, 120, 150, 200]
            selecao = st.selectbox('', ['Receita Mensal', 'Total de novos usuários mensal', 'Média de usuários ativos diários', 'Tickets'])
            
            if selecao == 'Receita Mensal':
                st.write(f'Total de receita R$: {sum(receita_mensal):,.2f}')
                st.plotly_chart(graf_barra(meses, receita_mensal, meses, ''), use_container_width=True)
                st.plotly_chart(graf_line(meses, receita_mensal, ''), use_container_width=True)
                st.plotly_chart(graf_pie(meses, receita_mensal, meses, ''), use_container_width=True)
            if selecao == 'Total de novos usuários mensal':
                st.write(f'Total de novos usuários {sum(novos_usuarios):,.0f}')
                st.plotly_chart(graf_barra(meses, novos_usuarios, meses, ''), use_container_width=True)
                st.plotly_chart(graf_line(meses, novos_usuarios, ''), use_container_width=True)
                st.plotly_chart(graf_pie(meses, novos_usuarios, meses, ''), use_container_width=True)
            if selecao == 'Média de usuários ativos diários':
                st.plotly_chart(graf_barra(meses, usuarios_ativos_diarios, meses, ''), use_container_width=True)
                st.plotly_chart(graf_line(meses, usuarios_ativos_diarios, ''), use_container_width=True)
                st.plotly_chart(graf_funil(meses, usuarios_ativos_diarios), use_container_width=True)
            if selecao == 'Tickets':
                st.write(f'Total de Tickets Abertos {sum(tickets_suporte_abertos):,.0f}')
                st.write(f'Total de Tickets Fechados {sum(tickets_suporte_fechados):,.0f}')
                st.plotly_chart(graf_barra_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados', 'Tickets Abertos X Fechados'), use_container_width=True)
                st.plotly_chart(graf_line_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados', 'Tickets Abertos X Fechados'), use_container_width=True)
                st.plotly_chart(graf_funil_agrupada(meses, tickets_suporte_abertos, tickets_suporte_fechados, 'Abertos','Fechados'), use_container_width=True)
                   
    with tab2:
        with st.spinner('CARREGANDO...'):
            def df_vendas():
                df = pd.read_excel(r'Excel/Vendas Consolidado.xlsx')

                df['Valor Unitario'] = df['Valor Unitario'].astype('float')
                df['Faturamento'] = df['Faturamento'].astype('float')
                df['Lucro'] = df['Lucro'].astype('float')

                df.drop_duplicates()

                df.drop(columns='Unnamed: 0', axis=0, inplace=True)

                return df

            df = df_vendas()

            st.subheader('Mude os filtros abaixo para atualizar os Dashboards')

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
            st.dataframe(dicionario)

            st.write('Click na legenda a direita para retirar as Barras ou as Linhas')    
            st.plotly_chart(graf_barra_linha(df_produto, 'Mês', 'Faturamento', 'Faturamento Mensal R$'), use_container_width=True)
            st.plotly_chart(graf_barra_linha(df_produto, 'Mês', 'Lucro', 'Lucro Mensal R$'), use_container_width=True)
            st.plotly_chart(graf_barra_linha(df_produto, 'Dia da semana', 'Faturamento', 'Faturamento por dia da semana R$'), use_container_width=True)
            st.plotly_chart(graf_barra_linha(df_produto, 'Dia da semana', 'Lucro', 'Lucro por dia da semana R$'), use_container_width=True)
            st.plotly_chart(graf_barra_agrupada2(df_produto, 'Mês', 'Faturamento', 'Loja', 'Comparação de Faturamento Mensal por Loja'), use_container_width=True)
            st.plotly_chart(graf_barra_agrupada2(df_produto, 'Mês', 'Faturamento', 'Produto', 'Comparação de Faturamento Mensal por Produto'), use_container_width=True)
            st.plotly_chart(graf_barra_count(df_produto, 'Mês', 'Produto', 'Quantidade de Produtos Vendidos por Mês'), use_container_width=True)
            st.plotly_chart(graf_barra_count(df_produto, 'Loja', 'Produto', 'Quantidade de Produtos Vendidos por Loja'), use_container_width=True)
            st.plotly_chart(graf_mapa(df_produto, 'Latitude', 'Longitude', 'Faturamento', 'Estado', 'Mapa dos Estados'), use_container_width=True)
            coluna1 , coluna2 = st.columns(2)
            coluna1.plotly_chart(graf_pie2(df_produto, 'Loja', 'Faturamento', 'Faturamento por Loja %'), use_container_width=True)
            coluna2.plotly_chart(graf_pie2(df_produto, 'Produto', 'Faturamento', 'Faturamento por Produto %'), use_container_width=True)
            coluna3 , coluna4 = st.columns(2)
            coluna3.plotly_chart(graf_pie2(df_produto, 'Loja', 'Lucro', 'Lucro por Loja %'), use_container_width=True)
            coluna4.plotly_chart(graf_pie2(df_produto, 'Produto', 'Lucro', 'Lucro por Produto %'), use_container_width=True)          

    with tab3:
        app_acoes()
    with tab4:
        st.subheader('EM ANDAMENTO LOGO ESTARÁ CONCLUÍDO.')
        st.subheader('ESSE É UM APP DE DASHBOARD ONDE VOCÊ FAZ UPLOAD DE UM ARQUIVO EXCEL E ELE VAI TENTAR MONTAR GRÁFICOS ULTIZANDO AS COLUNAS NÚMERICAS E DE TEXTO DO SEU ARQUIVO.')
        upload()   
