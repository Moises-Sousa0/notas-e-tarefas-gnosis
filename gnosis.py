import json
from prompt_toolkit import prompt
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
import tarefas


#caso o readline não funcione
try:
    import readline #linux
except ImportError:
    try:
        import pyreadline3 as readline #windows # type: ignore
    except ImportError:
        readline = None #ignora se n aceitar readline e pyread 


#carrega secoes
try:
    with open("secoes.json", "r", encoding="utf-8") as f:
        secoes = json.load(f)
except FileNotFoundError:
    secoes = {}
except json.JSONDecodeError:
    secoes = {}



menu_ver = """
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Anotações ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

gnosis_art = """
\033[1;31m
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
┃                                                                          ┃
┃                                                                          ┃
┃       ▄██████▄  ███▄▄▄▄    ▄██████▄     ▄████████  ▄█     ▄████████      ┃
┃      ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███      ┃
┃      ███    █▀  ███   ███ ███    ███   ███    █▀  ███▌   ███    █▀       ┃
┃     ▄███        ███   ███ ███    ███   ███        ███▌   ███             ┃
┃    ▀▀███ ████▄  ███   ███ ███    ███ ▀███████████ ███▌ ▀███████████      ┃
┃      ███    ███ ███   ███ ███    ███          ███ ███           ███      ┃
┃      ███    ███ ███   ███ ███    ███    ▄█    ███ ███     ▄█    ███      ┃
┃      ████████▀   ▀█   █▀   ▀██████▀   ▄████████▀  █▀    ▄████████▀       ┃
┃                                                                          ┃
┃                                                                          ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃                                                                          ┃ 
┃                           Version : v1.0 - Beta                          ┃
┃                           Update  : 23/09/2025                           ┃
┃                           Github  : https://github.com/Moises-Sousa0     ┃
┃                                                                          ┃ 
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[0m
\n\n"""

menu_art = """
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Gnosis Menu ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃                                                                          ┃
┃                                                                          ┃
┃   [1] - Adicionar Seção                                                  ┃
┃                                                                          ┃
┃   [2] - Adicionar Subtópico                                              ┃
┃                                                                          ┃
┃   [3] - Listar Seções e Subtópicos                                       ┃
┃                                                                          ┃
┃   [4] - Anotar                                                           ┃
┃                                                                          ┃
┃   [5] - Editar Nota                                                      ┃
┃                                                                          ┃
┃   [6] - Visualizar Nota                                                  ┃
┃                                                                          ┃
┃   [7] - Pesquisar por palavra                                            ┃
┃                                                                          ┃
┃   [8] - Remover                                                          ┃
┃                                                                          ┃
┃   [9] - Lista de Tarefas                                                 ┃
┃                                                                          ┃             
┃   [0] - Sair                                                             ┃
┃                                                                          ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃"""




def adicionar_secao():
    while True:
        tema = input("┃ Digite o nome da SEÇÂO: ").strip()
        if tema:
            break
        print("┃ Digite um nome válido")


    if tema in secoes:
        print("┃ Essa seção já existe")
    else:    
        secoes[tema] = {}
        print(f"┃ A seção {tema} foi criada!")

    with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
        json.dump(secoes, f, ensure_ascii=False, indent=4)
    return tema



def adicionar_subtopico():
    tema = input("┃ Digite o nome da SEÇÂO: ").strip()
    if tema not in secoes or not isinstance(secoes.get(tema), dict):
        print("┃ Essa seção não existe")
        return
    else:
        while True:
            subtopico = input("┃ Digite o nome do SUBTOPICO: ").strip()
            if subtopico:
                break 
            print("┃ Digite um nome válido")

        if subtopico in secoes[tema]:
            print("┃ Esse subtopico já existe")

        else:
            secoes[tema][subtopico] = []
            print(f"┃ O subtopico '{subtopico}' foi criado dentro de '{tema}' !")
    
    
    with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
        json.dump(secoes, f, ensure_ascii=False, indent=4)



def adicionar_anotaçao():
    listar()

    tema = input("\n\n┃ Digite o nome da seção onde deseja adicionar a anotação: ")
    if tema not in secoes:
        print("┃ Essa seção não existe")
        return
     
    subtopico = input("┃ Digite o nome do subtopico onde deseja adicionar a anotação: ")
    if subtopico not in secoes[tema]:
        print("┃ Esse subtopico não existe")
        return
    
    
    print(f"\n┃ Você está anotando em: \n┃ Seção: {tema} \n┃ Subtópico: {subtopico}\n")
    print("┃ Digite 'sair' para sair e salvar")
    print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Anotação ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
    while True:                                                                  
        linha = input("┃ ")
        if linha.lower() == "sair":
            break
        secoes[tema][subtopico].append(linha)
    
    with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
        json.dump(secoes, f, ensure_ascii=False, indent=4)


def listar():
    print("\n\n┃━━━━━━━━━━━━━━━━━━━━━━━━━━━ Seções-subtópicos ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
    for tema, subtopicos in secoes.items():
        print("┃")
        print(f"┃ Seção: {tema}")
        if subtopicos:
            for subtopico in subtopicos.keys():
                print(f"┗━ Subtópico: {subtopico}")
                
        else:
            print("┃ Sem subtópicos")



def edit_nota():
    listar()

    tema = input("\n\n┃ Digite o nome da seção: ")
    if tema not in secoes:
        print("┃ Essa seção não existe")
        return


    subtop = input("┃ Digite o nome do subtópico: ")
    if subtop not in secoes[tema]:
        print("┃ Esse subtópico não existe")
        return

    notas = secoes[tema][subtop]
    if not notas:
        print("┃ Esse subtópicos ainda não possui notas para editar :( ")
        return

    texto_atual = "\n".join(notas) #junta todos os textos e quebra a linha entre eles

    print(f"\n┃ Editando {subtop}")
    print("┃ Ctrl+S para salvar / Ctrl+C para cancelar\n")
    
    bindings = KeyBindings()  #variavel para guardar os atalhos / KeyBindings é uma classe do prompt toolkit

    @bindings.add("c-s") #ctrl+s salva
    def _(event): #evento do teclado
        secoes[tema][subtop] = event.app.current_buffer.text.splitlines()
        with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
            json.dump(secoes, f, ensure_ascii=False, indent=4)
        event.app.exit()

    @bindings.add("c-c") #ctrl+c cancela
    def _(event):
        event.app.exit()


    prompt( #abre o editor do prompttoolkits
        "┃ ",
        multiline=True, 
        default=texto_atual, #mostra o texto da nota para editar
        key_bindings=bindings #associa os atalhos criados
    )


def pesquisar():
    achou = False
    while True:
        pesquisa = input("┃ Digite a palavra que deseja achar: ").lower().strip()
        if pesquisa:
            break

        print("┃ Digite uma opção válida: ")
        

    print("")
    for tema, subtop in secoes.items():

        if pesquisa in tema.lower():
            print(f"┃ A palavra '{pesquisa}' está no nome da seção: '{tema}'\n")
            achou = True
        
        for sub, conteudo in subtop.items():
            if isinstance(sub, str) and pesquisa in sub.lower():
                print(f"┃ A palavra '{pesquisa}' está na seção: '{tema}' no nome do subtópico: '{sub}'")                    
                achou = True

            if isinstance(conteudo, list):
                for item in conteudo:
                     if isinstance(item, str) and pesquisa in item.lower():
                        print(f"┃ A palavra '{pesquisa}' está na seção: '{tema}' no subtópico: '{sub}'")
                        achou = True
                        break

    if not achou:    
        print(f"┃ '{pesquisa}' Não foi encontrada em nenhuma seção/subtópico")


def remover():
    while True:
        print("""┃ Opções para remover:
┃          
┃ 1 - Seção
┃ 2 - Subtópico
┃ 3 - Sair
┃          """)

        escolha_str = input("┃ Escolha uma opção: ").strip()
        if not escolha_str:
            print("┃ Por favor, digite um número \n")
            continue
        if not escolha_str.isdigit():
            print("┃ Entrada inválida, digite um número \n")
            continue

        escolha = int(escolha_str)

        if escolha == 1:
            if not secoes:
                print("┃ Nenhuma seção para remover")
                continue

            listar()
            apagar_secao = input("\n┃ Digite o nome da seção que você deseja apagar: ")

            if apagar_secao in secoes:
                secoes.pop(apagar_secao)    
                with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
                    json.dump(secoes, f, ensure_ascii=False, indent=4)
                    print(f"┃ A seção '{apagar_secao}' foi removida com sucesso!\n")
            else:
                print("┃ Essa seção não existe\n")
        
        elif escolha == 2:
            listar()
            nome_secao = input("\n┃ Digite o nome da seção: ")
            if nome_secao in secoes:
                sub_secao = secoes[nome_secao]
                if sub_secao:
                    apagar_subtopico = input("┃ Digite o nome do subtópico que você deseja apagar: ")
                    if apagar_subtopico in sub_secao:
                        sub_secao.pop(apagar_subtopico)
                        with open("secoes.json", "w", encoding="utf-8") as f: # Salva no arquivo JSON
                            json.dump(secoes, f, ensure_ascii=False, indent=4)
                        print(f"┃ O subtópico {apagar_subtopico} foi removido!\n")
                    else:
                        print("┃ Subtópico não encontrado nessa seção\n")
                else:
                    print("┃ Sem subtópicos\n")
            else:
                print("┃ Nome inválido ou inexistente\n")
        
        elif escolha == 3:
            break
        else:       
            print("┃ Opção inválida!\n")


def ver_nota():
    listar()

    tema = input("\n┃ Digite o nome da seção: ").strip()
    if tema not in secoes:
        print("┃ Essa seção não existe")
        return

    if not secoes[tema]:
        print("┃ Essa seção não possui subtópicos")
        return

    subtop = input("┃ Digite o nome do subtópico: ").strip()

    
    if subtop not in secoes[tema]:
        print("┃ Esse subtópico não existe")
        return

    notas = secoes[tema][subtop]
    if not notas:
        print("┃ Esse subtópico ainda não possui notas para editar :( ")
        return

    print(menu_ver)
    for nota in notas:
        for linha in nota.splitlines():
            linha = linha.strip()
            print(f"┃ {linha}")



def lista_tarefas():
    print


erro = ""
while True:
    print(gnosis_art)
    print(menu_art)
    if erro:
        print(f"┃ {erro}")
        erro = ""
    entrada = input("┃ Escolha uma opção: ").strip()
    if not entrada.isdigit():
        erro = "┃ Digite um número válido"
        continue
    print("┃━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("┃")

    escolha = int(entrada)

    if escolha == 1:
        adicionar_secao()
    elif escolha == 2:
        adicionar_subtopico()
    elif escolha == 3:
        listar()
    elif escolha == 4:
        adicionar_anotaçao()
    elif escolha == 5:
        edit_nota()
    elif escolha == 6:
        ver_nota()
    elif escolha == 7:
        pesquisar()
    elif escolha == 8:
        remover()
    elif escolha == 9:
        tarefas.menu_principal_tarefas()
    elif escolha == 0:
        print("Saindo...")
        break
    else:
        print("\nOpção inválida!\n")
        input("Aperte qualquer tecla para voltar ao menu: ")
        continue
        
    if escolha in [1, 2, 3, 4, 5, 6, 7, 8]:
        input("\n\n\nAperte qualquer tecla para voltar ao menu: ")