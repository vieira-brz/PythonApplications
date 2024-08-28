from business_rule_engine import RuleParser

# Define os parâmetros que serão avaliados pelas regras
params = {
    'products_in_stock': 10  # 
}

# Função que será chamada pela regra, que realiza a compra de mais itens
def order_more(items_to_order):
    print(f'You ordered {items_to_order} new items')
    return items_to_order

# Define as regras que serão processadas
rules = """
    rule "order new items"
    when
        AND(products_in_stock < 20,
        products_in_stock >= 5)
    then
        order_more(50)
    end

    rule "order new items urgent"
    when
        products_in_stock < 5,
    then
        AND(order_more(10, true),
        order_more(50))
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