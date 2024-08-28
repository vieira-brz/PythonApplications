from business_rule_engine import RuleParser
from business_rule_engine.exceptions import MissingArgumentError

# Define a função que será chamada se a regra for acionada
def order_more(items_to_order):
    return "you ordered {} new items".format(items_to_order)

# Define as regras
rules = """
rule "order new items"
when
    products_in_stock < 20  # Condição: verifica se o estoque é menor que 20
then
    order_more(50)  # Ação: solicita 50 novos itens
end
"""

# Define os parâmetros que serão avaliados pelas regras
params = {
    'products_in_stock': 10  # Estoque atual de produtos
}

# Cria uma instância do RuleParser
parser = RuleParser()

# Registra a função order_more no parser
parser.register_function(order_more)

# Interpreta a string de regras
parser.parsestr(rules)

# Itera sobre as regras no parser
for rule in parser:
    try:
        # Executa a regra com os parâmetros fornecidos
        rvalue_condition, rvalue_action = rule.execute(params)
        
        # Se a condição da regra for verdadeira, imprime a ação
        if rule.status:
            print(rvalue_action)
            break  # Interrompe o loop após a primeira regra válida
        
    except MissingArgumentError:
        pass  # Ignora exceções de argumento ausente
