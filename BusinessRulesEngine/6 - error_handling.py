from business_rule_engine import RuleParser

# Define a função que será chamada se a regra for acionada
def order_more(items_to_order):
    return "you ordered {} new items".format(items_to_order)

# Parâmetros de entrada com um erro de digitação proposital no nome da chave
params = {
    'produtcs_in_stock': 30  # Nota: a chave correta deve ser 'products_in_stock'
}

# Regras definidas para o mecanismo de regras
rules = """
rule "order new items"
when
    products_in_stock < 20
then
    order_more(50)
end
"""

# Cria uma instância do parser de regras
parser = RuleParser()

# Registra a função `order_more` no parser
parser.register_function(order_more)

# Faz o parsing das regras definidas
parser.parsestr(rules)

try:
    # Executa as regras com os parâmetros fornecidos
    ret = parser.execute(params)

    if ret is False:
        print("No conditions matched")  # Mensagem se nenhuma condição for atendida

except ValueError as e:
    # Captura e exibe erros de valor
    print(e)
