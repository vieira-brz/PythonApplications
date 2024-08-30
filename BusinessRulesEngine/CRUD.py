from pymongo import MongoClient


# Conecta ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['test']
rules_collection = db['rules']


def create_new_rule(name, condition, action):
    # Cria um dicionário representando a nova regra
    rule = {
        "name": name,
        "condition": condition,
        "action": action
    }

    # Verifica se a regra já existe no banco de dados
    already_in_db = rules_collection.find_one({'name': name})

    # Se a regra já existir, avisa o usuário
    if already_in_db:
        print(f'Regra "{name}" já cadastrada! Tente outro nome.')
    # Se a regra não existir, insere a nova regra no banco de dados
    else:
        rules_collection.insert_one(rule)
        print(f'Regra "{name}" criada com sucesso!')


def edit_rule(name, new_condition=None, new_action=None):
    # Prepara os campos que serão atualizados
    update_fields = {}

    if new_condition:
        update_fields['condition'] = new_condition

    if new_action:
        update_fields['action'] = new_action

    # Atualiza a regra existente no banco de dados
    result = rules_collection.update_one({"name": name}, {"$set": update_fields })

    # Verifica se a regra foi realmente editada
    if result.modified_count > 0:
        print(f'Regra "{name}" editada com sucesso!')
    else:
        print(f'Nenhuma condição/ação alterada para a regra "{name}".')


def delete_rule(name):
    # Deleta a regra do banco de dados
    result = rules_collection.delete_one({'name': name})

    # Verifica se a regra foi realmente deletada
    if result.deleted_count > 0:
        print(f'Regra "{name}" deletada com sucesso!')
    else:
        print(f'Nenhuma regra encontrada com o nome "{name}".')


def list_rules():
    # Busca todas as regras no banco de dados, excluindo o campo _id da saída
    rules = list(rules_collection.find({}, {'_id': 0}))

    # Verifica se há regras cadastradas
    if rules:
        for rule in rules:
            print(f'\nNome: {rule["name"]}\nCondição: {rule["condition"]}\nAção: {rule["action"]}')
    else:
        print('Nenhuma regra encontrada.')


def execute_rules(context):
    # Recupera todas as regras do banco de dados
    rules = rules_collection.find({})

    for rule in rules:
        condition = rule['condition']
        action = rule['action']

        # Verifica se a condição, fornecida como uma string, é verdadeira dentro do contexto definido
        # - condition: A condição a ser avaliada, passada como uma string.
        # - {}: Escopo global vazio, para evitar acesso a variáveis globais.
        # - context: Dicionário que define o escopo local, onde as variáveis e funções usadas na condição estão definidas.
        if eval(condition, {}, context):
            # Avalia e executa a ação, também fornecida como uma string, dentro do mesmo contexto
            # - action: A ação a ser executada.
            eval(action, {}, context)



#
# Exemplo de uso das funções
#
if __name__ == "__main__":
    # ----------------------------
    # Cria novas regras
    # 
    create_new_rule('Regra de Desconto', 'order_amount > 1000', 'apply_discount(10)')
    create_new_rule('Frete Grátis', 'customer_loyalty > 5', 'apply_free_shipping()')
    print('')

    # ----------------------------
    # Edita uma regra existente
    # 
    edit_rule('Regra de Desconto', new_condition='order_amount > 1500')
    print('')

    # ----------------------------
    # Lista todas as regras
    # 
    print('\n\nRegras:')
    list_rules()
    print('')

    # ----------------------------
    # Executa
    # 
    # Funções que podem ser chamadas pelas regras
    def apply_discount(percentage):
        print(f'Aplicando desconto de {percentage}%')

    def apply_free_shipping():
        print('Aplicando frete grátis')

    # Contexto para a execução das regras
    context = {
        'order_amount': 2000,
        'customer_loyalty': 6,
        'apply_discount': apply_discount,   # Inclui a função no contexto
        'apply_free_shipping': apply_free_shipping  # Inclui a função no contexto
    }  

    # Executa as regras no contexto dado
    print('\n\nExecutando regras:')
    execute_rules(context)
    print('')

    # ----------------------------
    # Deleta uma regra
    # 
    delete_rule('Frete Grátis')

    # ----------------------------
    # Lista todas as regras após a deleção
    # 
    print('\n\nRegras pós deleção:')
    list_rules()