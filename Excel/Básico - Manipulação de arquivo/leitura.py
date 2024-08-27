import openpyxl
from pathlib import Path

# Define ROOT_DIR como o diretório onde o script está sendo executado
ROOT_DIR = Path(__file__).parent.resolve()

# Carrega o arquivo de planilha existente 'Planilha Criada.xlsx'
book = openpyxl.load_workbook(ROOT_DIR / 'Planilha Criada.xlsx')

# Seleciona a aba 'Nome_planilha' para manipulação
book_page = book['Nome_planilha']

# Itera sobre as linhas da planilha, da linha 2 até a linha 4
for rows in book_page.iter_rows(min_row=2, max_row=4):
    for cell in rows:
        # Verifica se a célula contém o valor 'item 1'
        if cell.value == 'item 1':
            # Se encontrar, substitui o valor por 'item 0'
            cell.value = 'item 0'

# Salva as alterações na mesma planilha 'Planilha Criada.xlsx'
book.save(ROOT_DIR / 'Planilha Criada.xlsx')