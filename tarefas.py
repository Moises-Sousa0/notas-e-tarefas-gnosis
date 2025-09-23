import json


#caso o readline não funcione
try:
    import readline #linux
except ImportError:
    try:
        import pyreadline3 as readline #windows # type: ignore
    except ImportError:
        readline = None #ignora se n aceitar readline e pyread 


#carrega tarefas
def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(" Arquivo corrompido, criando um novo...")
        return {}
        
    

#salva tarefas 
def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)


tarefas = carregar_tarefas()


menu_tarefas = """
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Menu Tarefas ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃                                                                          ┃
┃                                                                          ┃
┃   [1] - Adicionar Categoria                                              ┃
┃                                                                          ┃
┃   [2] - Adicionar tarefa a uma categoria                                 ┃
┃                                                                          ┃
┃   [3] - Atualizar status da tarefa                                       ┃
┃                                                                          ┃
┃   [4] - Listar tarefas por categoria                                     ┃
┃                                                                          ┃
┃   [5] - Remover tarefa                                                   ┃
┃                                                                          ┃
┃   [0] - Sair                                                             ┃                                                       
┃                                                                          ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
"""





def adicionar_categoria():
    while True:
        categoria = input("┃ Digite o nome da categoria: ").strip()
        if categoria:
            break
        else:
            print("┃ Digite um nome válido")
    
    if categoria in tarefas:
        print("┃ Essa categoria já existe")
    else:
        tarefas[categoria] = []
        print(f"┃ A categoria '{categoria}' foi criada")
        salvar_tarefas(tarefas)


def adicionar_tarefa():
    categorias = listar_categorias()
    if not categorias:
        return
    
    cat_str = input("\n┃ Digite o número da categoria: ").strip()
    if not cat_str.isdigit():
        print("┃ Entrada inválida")
        return

    cat_num = int(cat_str) - 1
    if cat_num < 0 or cat_num >= len(categorias):
        print("┃ Número de categoria inválido")
        return

    categoria = categorias[cat_num]
    tarefa = input("┃ Digite a tarefa: ").strip()
    if not tarefa:
        print("┃ Tarefa vazia não pode ser adicionada")
        return
    
    tarefas[categoria].append({"titulo": tarefa, "status": "Pendente"})
    print(f"┃ Tarefa adicionada à categoria '{categoria}' com sucesso!")
    salvar_tarefas(tarefas)

def listar_tarefas_da_categoria(categoria):
    lista_tarefas = tarefas[categoria]
    if not lista_tarefas:
        print("┃ (Vazio)")
        return
    
    print("━" * 40)
    print("┃ Tarefas Disponíveis: ")
    print("┃")
    for i, tarefa in enumerate(lista_tarefas, 1):
        print(f"┃ [{i}] [{tarefa['status']}] {tarefa['titulo']}")


def atualizar_status():
    if not tarefas:
        print("┃ Nenhuma categoria cadastrada")
        return
    
    
    listar_categorias()
    print()
    categoria_str = input("\n\n┃ Digite o número da categoria da tarefa que deseja atualizar: ").strip()
    if not categoria_str.isdigit():
        print("┃ Entrada inválida")
        return
    
    cat_num = int(categoria_str) - 1
    categorias = list(tarefas.keys())

    if cat_num < 0 or cat_num >= len(categorias):
        print("┃ Número de categoria inválido")
        return

    categoria = categorias[cat_num]

    if not tarefas[categoria]:
        print("┃ Essa categoria não tem tarefas")
        return


    listar_tarefas_da_categoria(categoria)
    tarefa_str = input("\n┃ Qual tarefa deseja atualizar? ").strip()
    if not tarefa_str.isdigit():
        print("┃ Entrada inválida")
        return

    tarefa_num = int(tarefa_str) - 1
    if tarefa_num < 0 or tarefa_num >= len(tarefas[categoria]):
        print("┃ Número de tarefa inválido")
        return


    tarefa_selecionada = tarefas[categoria][tarefa_num]
    tarefa_selecionada['status'] = "Concluida" if tarefa_selecionada['status'] == "Pendente" else "Pendente"

    print(f"┃ Tarefa '{tarefa_selecionada['titulo']}' atualizada para [{tarefa_selecionada['status']}]")
    salvar_tarefas(tarefas)



def listar_tarefas():
    if not tarefas:
        print("┃ Nenhuma tarefa registrada")
        return

    for categoria, listade_tarefas in tarefas.items():
        print()
        print("━" * 40)
        print(f"┃ Categoria: {categoria}")
        if not listade_tarefas:
            print("┃ (Vazio)")
        else:
            for i, tarefa in enumerate(listade_tarefas, 1):
                print(f"┃ [{i}] [{tarefa['status']}] {tarefa['titulo']}")
        print()

def listar_categorias():
    if not tarefas:
        print("┃ Nenhuma categoria registrada")
        return []

    print("━" * 40)
    print("┃ Categorias Disponíveis:")
    print("┃")
    categorias = list(tarefas.keys())
    for i, categoria in enumerate(categorias, 1):
        print(f"┃ [{i}] {categoria}")
    return categorias


def remover():
    while True:
        print("""\n┃ Opções para remover:
┃ 1 - Categoria
┃ 2 - Tarefa
┃ 3 - Sair""")
        
        escolha = input("┃ Escolha uma opção: ").strip()
        if not escolha.isdigit():
            print("┃ Entrada inválida")
            continue
        escolha = int(escolha)

        if escolha == 1:
            categorias = listar_categorias()
            if not categorias:
                continue

            cat_str = input("\n┃ Número da categoria que deseja remover: ").strip()
            if not cat_str.isdigit():
                print("┃ Entrada inválida")
                continue

            cat_num = int(cat_str) - 1
            if cat_num < 0 or cat_num >= len(categorias):
                print("┃ Número de categoria inválido")
                continue

            categoria = categorias[cat_num]
            del tarefas[categoria]
            print(f"┃ Categoria '{categoria}' removida com sucesso!")
            salvar_tarefas(tarefas)

        elif escolha == 2:
            categorias = listar_categorias()
            if not categorias:
                continue

            cat_str = input("\n┃ Número da categoria da tarefa: ").strip()
            if not cat_str.isdigit():
                print("┃ Entrada inválida")
                continue

            cat_num = int(cat_str) - 1
            if cat_num < 0 or cat_num >= len(categorias):
                print("┃ Número de categoria inválido")
                continue

            categoria = categorias[cat_num]
            if not tarefas[categoria]:
                print("┃ Essa categoria não tem tarefas")
                continue

            listar_tarefas_da_categoria(categoria)
            tarefa_str = input("\n┃ Número da tarefa que deseja remover: ").strip()
            if not tarefa_str.isdigit():
                print("┃ Entrada inválida")
                continue

            tarefa_num = int(tarefa_str) - 1
            if tarefa_num < 0 or tarefa_num >= len(tarefas[categoria]):
                print("┃ Número de tarefa inválido")
                continue

            tarefa_removida = tarefas[categoria].pop(tarefa_num)
            print(f"┃ Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")
            salvar_tarefas(tarefas)

        elif escolha == 3:
            break
        else:
            print("┃ Opção inválida")



def menu_principal_tarefas():
    while True:
        print(menu_tarefas)
        print()
        opcao_str = input("┃ Digite sua opção: ").strip()
        print()
        
        if not opcao_str.isdigit():
            print("┃ Digite um número válido\n")
            continue

        opcao = int(opcao_str)

        if opcao == 1:
            adicionar_categoria()
        elif opcao == 2:
            adicionar_tarefa()
        elif opcao == 3:
            atualizar_status()
        elif opcao == 4:
            listar_tarefas()
        elif opcao == 5:
            remover()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("\nOpção inválida!\n")
            input("Aperte qualquer tecla para voltar ao menu: ")
            continue

        if opcao in [1, 2, 3, 4, 5,]:
            input("\n\n\nAperte qualquer tecla para voltar ao menu: ")



if __name__ == "__main__":
    menu_principal_tarefas()