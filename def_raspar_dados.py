from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

def raspar_dados(palavra__chave):
    palavra_chave = palavra__chave

    if palavra_chave == None:
        pass
    else:    
        #chrome_options = Options()
        #chrome_options.add_argument("--start-minimized")
        #chrome_options.add_argument("--headless")  # Executar em modo headless
        #chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU (recomendado para headless)

        navegador = webdriver.Chrome()#options=chrome_options)
        navegador.minimize_window()
        actions = ActionChains(navegador)

        def espera_elemento(tipo, elemento):
            if tipo == "ID":
                WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, elemento)))
            elif tipo == "XPATH":
                WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, elemento)))
            elif tipo == "CLASS_NAME":
                WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.CLASS_NAME, elemento))) 
        
        #ACESSANDO O SITE DO MERCADO LIVRE
        navegador.get(r'https://www.mercadolivre.com.br/')

        espera_elemento("ID", "cb1-edit")
        navegador.find_element(By.ID, 'cb1-edit').send_keys(palavra_chave)
        actions.send_keys(Keys.ENTER).perform()

        #PEGANDO O XPAHT PRINCIPAL DA LISTA DE RESULTADOS
        espera_elemento('XPATH', '/html/body/main/div/div[2]/section')
        espera_elemento('XPATH', '/html/body/main/div/div[2]/section/ol')
        elementos = navegador.find_elements(By.XPATH, '/html/body/main/div/div[2]/section/ol')  
        lista_elementos = []

        for ele in elementos:
            lista_elementos.append(ele.find_elements(By.CLASS_NAME, 'poly-card__content'))

        # PEGANDO O TITULO DE CADA ELEMENTO ENCONTRADO
        lista_titulos = []
        for i, ele in enumerate(lista_elementos[0]):
            try:
                lista_titulos.append(ele.find_element(By.TAG_NAME, 'h3').text)
            except:
                continue

        #PEGANDO O LINK DE CADA ELEMENTO
        lista_links = []
        for i, ele in enumerate(lista_elementos[0]):
            try:
                lista_links.append(ele.find_element(By.TAG_NAME, 'a').get_attribute('href'))
            except:
                continue

        #PEGANDO AS IMAGENS DE CADA ITEM
        lista_imagens = []
        lista_elementos_img = navegador.find_elements(By.CLASS_NAME, 'poly-card__portada')
        for ele in lista_elementos_img:
            lista_imagens.append(ele.find_element(By.TAG_NAME, 'img').get_attribute('src'))

        # PEGANDO O PREÇO DE CADA ITEM
        lista_precos = []
        for i, ele in enumerate(lista_elementos[0]):
            try:
                preco = ele.find_elements(By.CLASS_NAME, 'poly-price__current')
                lista_precos.append(preco[0].find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text)
            except:
                continue

        #PASSANDOS OS 10 PRIMEIROS ITEMS PARA UM DATAFRAME
        df_1 = pd.DataFrame({
            'Site' : 'Mercado Livre',
            'Imagem_Produto' : lista_imagens[0:11],
            'Produtos': lista_titulos[0:11],
            'Preco_a_Vista': lista_precos[0:11],
            'Link_Produto': lista_links[0:11]
        })

        #ACESSANDO O SITE DA MAGAZINE LUIZA
        navegador.get(r'https://www.magazineluiza.com.br/')
        espera_elemento('ID', 'input-search')
        navegador.find_element(By.ID, 'input-search').send_keys(palavra_chave)
        sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        espera_elemento('CLASS_NAME', 'bgvRHR')
        sleep(1)
        lista_elementos = navegador.find_elements(By.CLASS_NAME, 'bgvRHR')
        lista_elementos = lista_elementos[0].find_elements(By.TAG_NAME, 'li')

        #PEGANDO O LINK DE CADA ELEMENTO
        lista_links = []
        for i, ele in enumerate(lista_elementos):
            try:
                lista_links.append(ele.find_element(By.TAG_NAME, 'a').get_attribute('href'))
            except:
                continue

        #PEGANDO AS IMAGENS DE CADA PRODUTO
        lista_imagens = []
        for ele in lista_elementos:
            lista_imagens.append(ele.find_element(By.TAG_NAME, 'img').get_attribute('src'))

        #PEGANDO O NOME DO PRODUTO
        lista_titulos = []
        for ele in lista_elementos:
            elemento = ele.find_element(By.TAG_NAME, 'a')
            elemento = ele.find_elements(By.TAG_NAME, 'h2')
            lista_titulos.append(elemento[0].text)

        #PEGANDO O PREÇO DOS PRODUTOS
        lista_precos = []
        lista_precos_final = []
        for ele in lista_elementos:
            elemento = ele.find_elements(By.TAG_NAME, 'a')  
            lista_precos.append(elemento)
        for ele in lista_precos:
            lista_precos_final.append(ele[0].find_element(By.CLASS_NAME, 'kqgDtZ').text)

        for i, ele in enumerate(lista_precos_final):
            lista_precos_final[i] = lista_precos_final[i].replace("ou R$ ", "")
            lista_precos_final[i] = lista_precos_final[i].replace("\nno Pix", "")
            lista_precos_final[i] = lista_precos_final[i].replace(",", ".")

        #PASSANDOS OS 10 PRIMEIROS ITEMS PARA UM DATAFRAME
        df_2 = pd.DataFrame({
            'Site' : 'Magazine Luiza',
            'Imagem_Produto' : lista_imagens[0:11],
            'Produtos': lista_titulos[0:11],
            'Preco_a_Vista': lista_precos_final[0:11],
            'Link_Produto': lista_links[0:11]
        })

        navegador.quit()
        df_final = pd.concat([df_1, df_2], ignore_index=True)
        df_final['Preco_a_Vista'] = df_final['Preco_a_Vista'].replace(".", "")
        df_final['Preco_a_Vista'] = df_final['Preco_a_Vista'].replace("R$", "")
        df_final['Preco_a_Vista'] = df_final['Preco_a_Vista'].str.strip()        
        return df_final