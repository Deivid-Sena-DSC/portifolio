import streamlit as st
from streamlit_option_menu import option_menu
from Paginas import home_page, page1, page2, page3
import time

st.set_page_config(layout="wide")

carregando = st.empty()
carregando.progress(50, "Carregando")
time.sleep(1)
carregando.progress(100, "Tudo Pronto")
time.sleep(1)
carregando.empty()


# Função principal de navegação
def main():
    img_url = "https://img.freepik.com/vetores-gratis/linha-onda-de-estilo-minimalista-de-cor-gradiente-de-luxo_483537-3948.jpg?t=st=1732553142~exp=1732556742~hmac=8a7a708bf5fb6b7624a9d4f7ff59ff60c268ac7a27946063c9486164e73845e1&w=1060"
    # HTML para definir a imagem de fundo
    background_image = f"""<style>.stApp {{
        background-image: url("{img_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        }}</style>"""
    # Aplicar o estilo de fundo
    st.markdown(background_image, unsafe_allow_html=True)

    # Barra lateral para navegação
    st.sidebar.image(r'imagens\dsc.jpg')
  
    with st.sidebar:
            page = option_menu(
                                menu_title = "Escolha uma página",
                                options = ["Home", "Experiência Profissional", "Formação Acadêmica", "Portifólio", 'Contato'],
                                menu_icon=None,
                                icons=['house', 'pc-display-horizontal', 'book', 'bank','envelope'])

    # Exibir o conteúdo baseado na página selecionada
    if page == "Home":
        home_page()
    elif page == "Experiência Profissional":
        page1()
    elif page == "Formação Acadêmica":
        page2()
    elif page == "Portifólio":
        page3()


# Rodar a função principal
if __name__ == "__main__":
    main()

    # streamlit run CV_DSC.py
