from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent

# Caminho para a pasta onde o chromedriver está localizado
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# Função para criar uma instância do navegador Chrome com opções adicionais
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()  # Configurações de opções do Chrome

    # Adiciona opções ao navegador, se houver
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # Adiciona cada opção passada como argumento

    # Define o serviço para usar o chromedriver
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),  # Especifica o caminho do chromedriver
    )

    # Cria uma instância do navegador Chrome
    browser = webdriver.Chrome(
        service=chrome_service,  # Usa o serviço definido
        options=chrome_options   # Aplica as opções configuradas
    )

    return browser  # Retorna o navegador configurado

if __name__ == '__main__':
    TIME_TO_WAIT = 10  # Tempo de espera em segundos

    options = ()  # Exemplo de opções (atualmente vazio)
    browser = make_chrome_browser(*options)  # Cria o navegador com as opções especificadas

    browser.get('https://www.google.com')  # Acessa o site do Google

    # Espera para encontrar o campo de busca do Google
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')  # Localiza o campo de busca pelo atributo 'name'
        )
    )

    search_input.send_keys('Hello World!')  # Digita "Hello World!" no campo de busca
    search_input.send_keys(Keys.ENTER)      # Envia o texto digitado no campo de busca

    # Encontra a seção de resultados de pesquisa
    results = browser.find_element(By.ID, 'search')  # Localiza a seção de resultados pelo ID 'search'
    links = results.find_elements(By.TAG_NAME, 'a')  # Encontra todos os links dentro da seção de resultados

    links[0].click()  # Clica no primeiro link da lista de resultados

    sleep(TIME_TO_WAIT)  # Espera 10 segundos antes de encerrar o script
