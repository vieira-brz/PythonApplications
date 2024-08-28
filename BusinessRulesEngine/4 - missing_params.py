from business_rule_engine import RuleParser

# Inicializa os parâmetros como um dicionário vazio
params = {}

# Função que será chamada pela regra, que realiza a compra de mais itens
def order_more(items_to_order):
    print(f'You ordered {items_to_order} new items')
    return items_to_order

# Define as regras para o motor de regras
rules = """
rule "order new items"
when
    products_in_stock < 20 
then
    order_more(50)  
end
"""

# Cria uma instância do RuleParser
parser = RuleParser()

# Registra a função order_more no parser (essa função deve estar definida em algum lugar no código)
parser.register_function(order_more)

# Interpreta as regras definidas
parser.parsestr(rules)

# Executa o motor de regras com os parâmetros fornecidos
# set_default_arg=True permite que o motor utilize valores padrão para parâmetros ausentes
# default_arg=0 define que o valor padrão será 0
parser.execute(params, set_default_arg=True, default_arg=0)
