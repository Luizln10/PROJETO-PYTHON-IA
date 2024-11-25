tarefas = {
    1: {'descricao': 'Fazer compras', 'prioridade': 'Alta', 'categoria': 'Compras'}, 
    2: {'descricao': 'Trabalhar', 'prioridade': 'Média', 'categoria': 'Trabalho'}, 
    3: {'descricao': 'Almoçar', 'prioridade': 'Alta', 'categoria': 'Alimento'},
    4: {'descricao': 'Treinar', 'prioridade': 'Baixa', 'categoria': 'Saúde'}
}

categorias = set()
prioridades = set()

def adicionar_tarefa(descricao, prioridade, categoria):
    id_tarefa = len(tarefas) + 1
    nova_tarefa = {
        'ID': id_tarefa,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
    }
    tarefas[id_tarefa] = nova_tarefa
    categorias.add(categoria)
    prioridades.add(prioridade)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def exibir_tarefas():
    for id_tarefa, detalhes in tarefas.items():
        print(f"ID: {id_tarefa}, Descrição: {detalhes['descricao']}, Prioridade: {detalhes['prioridade']}, Categoria: {detalhes['categoria']}")

def remover_tarefa(id_tarefa):
    if id_tarefa in tarefas:
        del tarefas[id_tarefa]
        print(f"Tarefa com ID {id_tarefa} removida com sucesso!")
    else:
        print("Tarefa não encontrada!")

def buscar_tarefas_por_categoria(categoria): 
    for tarefa_da_vez in tarefas:
        print(f"""
    ID: {tarefa_da_vez['ID']}
    Categoria: {tarefa_da_vez['categoria']}
    """)
    nome_tarefa = input("Digite o nome da categoria: ")
    for tarefa_da_vez in tarefas:
        if tarefa_da_vez['categoria'] == nome_tarefa:
            print(f"""
          ID: {tarefa_da_vez['ID']}
          Categoria: {tarefa_da_vez['categoria']}
          """)
    return {id_tarefa: detalhes for id_tarefa, detalhes in tarefas.items() if detalhes['categoria'] == categoria}
def buscar_tarefas_por_prioridade(prioridade): 
    return {id_tarefa: detalhes for id_tarefa, detalhes in tarefas.items() if detalhes['prioridade'] == prioridade}

def menu():
    print("\nMenu de Gerenciamento de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Exibir todas as tarefas")
    print("3. Remover tarefa")
    print("4. Buscar tarefas por categoria")
    print("5. Buscar tarefas por prioridade")
    print("6. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Digite a descrição da tarefa: ")
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
        categoria = input("Digite a categoria: ")
        adicionar_tarefa(descricao, prioridade, categoria)
    elif escolha == '2':
        exibir_tarefas()
    elif escolha == '3':
        id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
        remover_tarefa(id_tarefa)
    elif escolha == '4':
        categoria = input("Digite a categoria: ")
        tarefas_categoria = buscar_tarefas_por_categoria(categoria)
        for tarefa in tarefas_categoria:
            print(f"ID: {tarefa['ID']} Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}")
    elif escolha == '5':
        prioridade = input("Digite a prioridade: ")
        tarefas_prioridade = buscar_tarefas_por_prioridade(prioridade)
        for tarefas in tarefas_prioridade:
            print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Prioridade: {tarefa[2]}, Categoria: {tarefa[3]}")
    elif escolha == '6':
        print("Saindo do programa")
        break
    else:
        print("Opção inválida! Tente novamente")
