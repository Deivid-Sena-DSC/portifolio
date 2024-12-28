import streamlit as st
from streamlit_option_menu import option_menu 
from Paginas1_2 import home_page, page1, page2
from Pagina3 import page3
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
    img_url = "https://images5.alphacoders.com/301/301407.jpg"
    # HTML para definir a imagem de fundo
    background_image = f"""<style>.stApp {{
        background-image: url("{img_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        }}</style>"""
    # Aplicar o estilo de fundo
    st.markdown(background_image, unsafe_allow_html=True)

    
    with st.sidebar:
            page = option_menu(
                                menu_title = False,
                                options = ["Home", "Experiência Profissional", "Formação Acadêmica", "Portifólio"],
                                menu_icon=None,
                                icons=['house', 'pc-display-horizontal', 'book', 'bank'])
            
            st.subheader('Contato')
            st.link_button('LinkedIn', url='https://www.linkedin.com/in/deivid-sena-dsc/')
            st.write('Tel: (11) 97529-1160')
            st.write('deivid.sena.dsc@gmail.com')

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

    # streamlit run Portifolio.py
