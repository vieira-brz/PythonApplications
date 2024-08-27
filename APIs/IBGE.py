import requests

# Link para a API do IBGE que fornece os dados
link = "https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/2014/variaveis/10484?localidades=N1[all]"

# Faz uma requisição GET para o link fornecido
req = requests.get(link)

# Converte a resposta da requisição em formato JSON
informacoes = req.json()

# Busca o nome da variável dentro das informações obtidas
item_busca = informacoes[0]['variavel']

# Exibe o nome da variável
print(item_busca + '\n')

# Itera sobre a lista de classificações para obter os nomes e quantidades
for i in range(len(informacoes[0]['resultados'][0]['classificacoes'])):
    # Extrai o nome da classificação
    nome = informacoes[0]['resultados'][0]['classificacoes'][i]['nome']
    
    # Extrai as chaves das categorias dentro da classificação (quantidades)
    qtd = list(informacoes[0]['resultados'][0]['classificacoes'][i]['categoria'].keys())[0]

    # Extrai a unidade de medida
    unidade = informacoes[0]['unidade']

    # Exibe o nome da classificação e a primeira quantidade
    print(f'{nome} = {qtd} {unidade}')