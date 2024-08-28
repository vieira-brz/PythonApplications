from business_rule_engine import RuleParser

# Função para verificar se um número é par
def is_even(num):
    if (num % 2) == 0:
        return True
    return False

# Função personalizada para imprimir uma mensagem
def custom_print(message):
    print(message)

# Parâmetros de entrada, onde 'number' é o valor a ser avaliado
params = {
    'number': 10
}

# Regras definidas para o motor de regras
rules = """
    rule 'check even number'
    when 
        is_even(number) = True 
    then
        custom_print("is even")
    end
"""

# Instancia o parser de regras
parser = RuleParser()

# Registra as funções personalizadas no parser
parser.register_function(is_even)
parser.register_function(custom_print)

# Interpreta as regras definidas
parser.parsestr(rules)

# Executa o motor de regras com os parâmetros fornecidos
parser.execute(params)