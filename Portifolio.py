import streamlit as st
from streamlit_option_menu import option_menu 
from Paginas1_2 import page1, page2
from Home import home_page
import time

st.set_page_config(layout="wide")

# Função principal de navegação
def main():
    img_url = "https://wallpapers.com/images/hd/1920x1080-black-ivgflkhu7bxomm84.jpg"
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
                                options = ["Home - Portifólio", "Experiência Profissional", "Formação Acadêmica"],
                                menu_icon=None,
                                icons=['bank', 'pc-display-horizontal', 'book'])
            
            st.subheader('Contato')
            st.link_button('LinkedIn', url='https://www.linkedin.com/in/deivid-sena-dsc/')
            st.write('Tel: (11) 97529-1160')
            st.write('deivid.sena.dsc@gmail.com')

    # Exibir o conteúdo baseado na página selecionada
    if page == "Home - Portifólio":
        home_page()
    elif page == "Experiência Profissional":
        page1()
    elif page == "Formação Acadêmica":
        page2()


# Rodar a função principal
if __name__ == "__main__":
    main()

# streamlit run Portifolio.py