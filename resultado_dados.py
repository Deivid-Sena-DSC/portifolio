import streamlit as st
from def_raspar_dados import raspar_dados


def resultado_dados():

    chave = st.text_input('Insira uma palavra chave para busca')

    if len(chave) == 0:
        st.markdown('Aguardando palavra chave')
    elif len(chave) >= 1:
        with st.spinner('CARREGANDO'):
            df = raspar_dados(chave)
            st.dataframe(df, column_config={"Imagem_Produto": st.column_config.ImageColumn("Imagem_Produto"),
                                            "Preco_a_Vista": st.column_config.NumberColumn("Preco_a_Vista"),
                                            "Link_Produto": st.column_config.LinkColumn("Link_Produto")},
                                                use_container_width=True)

    # streamlit run resultado_dados.py