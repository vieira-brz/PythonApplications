import requests

# Solicita ao usuário que insira o CEP
cep = input('Digite seu CEP: ').replace('-', '').replace('.', '').replace(' ', '').strip()

# Verifica se o CEP tem exatamente 8 dígitos
if len(cep) == 8:
    # Monta o link da API utilizando o CEP fornecido
    link = f'https://viacep.com.br/ws/{cep}/json/'

    # Faz a requisição GET para o link fornecido
    req = requests.get(link)

    # Converte a resposta da requisição em um dicionário (JSON)
    dic_req = req.json()

    # Extrai as informações do dicionário retornado pela API
    uf = dic_req['uf']
    logradouro = dic_req['logradouro']
    cidade = dic_req['localidade']
    bairro = dic_req['bairro']
    
    # Exibe o endereço formatado
    print(f'Seu endereço é: {logradouro}, {bairro}, {cidade} - {uf}')
else:
    # Caso o CEP não tenha 8 dígitos, exibe uma mensagem de erro
    print('CEP inválido!')