from business_rule_engine import RuleParser

# Define os parâmetros que serão avaliados pelas regras
params = {
    'products_in_stock': 10  
}

# Função que será chamada pela regra, que realiza a compra de mais itens
def order_more(items_to_order):
    print(f'You ordered {items_to_order} new items')
    return items_to_order

# Define as regras que serão processadas
rules = """
    rule "order new items"
    when 
        products_in_stock < 20  # Condição: se os produtos em estoque forem menores que 20
    then
        order_more(50)  # Ação: realiza o pedido de 50 novos itens
    end
"""

# Cria um objeto RuleParser que vai interpretar e executar as regras
parser = RuleParser()

# Registra a função `order_more` para que possa ser chamada pelas regras
parser.register_function(order_more)

# Analisa a string contendo as regras
parser.parsestr(rules)

# Executa as regras passando os parâmetros definidos em `params`
parser.execute(params)