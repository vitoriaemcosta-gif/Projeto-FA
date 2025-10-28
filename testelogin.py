# # Lista global para armazenar as credenciais (email e senha).
# # Mover esta lista para fora das funções é o principal ponto de correção.
# cad_dados = []
# login_dados = []

# def verificar(entrar) :
#     if entrar == 1:
#         menu()
#         print()
#     elif entrar == 0:
#         print("Email ou senha incorretos. Tente novamente.")
#         login()

# # Função 'menu' fictícia, pois não estava definida no código original
# def menu():
#     print("Bem-vindo ao menu principal do FEIFOOD!")

# def usuario() :
#     global login_dados # Indica que vamos usar a lista global
#     global cad_dados # Indica que vamos usar a lista global

#     print("Seja Bem vindo(a) ao FEIFOOD !!! ")
    
#     # Substituindo try/except por um loop while para garantir a entrada
#     while True:
#         # Pede a entrada como string
#         user_input = input("• Digite 1 para realizar o seu cadastro ou 2 para realizar login: ")
        
#         if user_input in ('1', '2'):
#             user = int(user_input) # Converte para inteiro apenas se for válido
#             break # Sai do loop
#         else:
#             print("Opção inválida. Por favor, digite apenas 1 ou 2.")

#     if user == 1:
#         # Bloco de Cadastro
#         cadnm = input("Digite seu nome: ")
#         # Atenção: Se o usuário digitar letras aqui, o programa ainda falhará,
#         # pois não estamos tratando o erro com try/except.
#         cadtl = int(input("Digite seu telefone: ")) 
#         cadem = input("Digite seu email: ")
#         cadsn = input("Digite sua senha (com até 5 letras) : ")
        
#         # 1. Salva as credenciais na lista global
#         cad_dados.append(cadnm)    
#         cad_dados.append(cadtl)
#         login_dados.append(cadem)
#         login_dados.append(cadsn)

#         print()
#         print("Cadastro realizado com sucesso !!!\nFaça o login para acessar o FEIFOOD. \n")
        
#         # Chama o login após o cadastro
#         verificar(login()) 

#     elif user == 2:
#         # Chama o login se a opção for 2
#         verificar(login())


# def login():
#     global login_dados
    
#     if not login_dados: 
#         print("Nenhum usuário cadastrado. Por favor, cadastre-se primeiro.")
#         return 0 # Retorna 0 (falha)

#     loginem = input("Digite seu email: ")
#     loginsn = input("Digite sua senha: ")

#     # Percorre a lista de credenciais global (email, senha, email, senha, ...)
#     for i in range(0, len(login_dados), 2):
#         # Compara o email e a senha digitados com os pares na lista
#         if loginem == login_dados[i] and loginsn == login_dados[i+1]:
#             return 1 # Encontrado: Sucesso

#     # Se o loop terminar sem encontrar a credencial
#     return 0 # Falha

# # Chama a função inicial
# usuario()


def alimentos():
    
    # ------------------------------------------------------------------
    # DADOS (Mantidos conforme sua estrutura original)
    # ------------------------------------------------------------------
    
    # PIZZAS
    queijo = {'Descrição: ' : 'Clássica pizza de massa fina, coberta com molho de tomate e generosa camada de mussarela;',
              'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas;',
              'Valor: ' : 'R$60,00'}
    calabresa = {'Descrição: ' : 'Pizza tradicional com molho de tomate, mussarela, fatias de linguiça calabresa e cebola;',
                 'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas.',
                 'Valor: ' : 'R$65,00'}
    quatro_queijos = {'Descrição: ' : 'Mussarela, provolone, parmesão e requeijão cremoso.',
                      'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas.',
                      'Valor: ' : 'R$68,00'}
    frango_catupiry = {'Descrição: ' : 'Peito de frango desfiado, temperado e coberto com catupiry original.',
                       'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas.',
                       'Valor: ' : 'R$70,00'}

    # HAMBÚRGUERES
    tradicional = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo, alface e tomate;',
                   'Porção: ' : '1 pessoa;',
                   'Valor: ' : 'R$22,00'}
    bacon = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo e fatias de bacon crocante;',
             'Porção: ' : '1 pessoa;',
             'Valor: ' : 'R$27,00'}
    duplo = {'Descrição: ' : 'Pão, dois hambúrgueres de 150g, queijo cheddar e molho especial.',
             'Porção: ' : '1 pessoa;',
             'Valor: ' : 'R$35,00'}

    # MARMITAS
    frango_marmita = {'Descrição: ' : 'Marmita com filé de peito de frango grelhado, acompanhado de arroz, feijão e batata frita;',
                      'Porção: ' : '1 pessoa;',
                      'Valor: ' : 'R$27,00'}
    tilapia = {'Descrição: ' : 'Marmita com filé de peixe Tilápia grelhado, assado ou frito, acompanhado de arroz e salada;',
               'Porção: ' : '1 pessoa;',
               'Valor: ' : 'R$27,00'}
    carne_bovina = {'Descrição: ' : 'Marmita com Bife Acebolado, acompanhado de arroz, feijão, farofa e couve refogada.',
                    'Porção: ' : '1 pessoa;',
                    'Valor: ' : 'R$32,00'}

    # ------------------------------------------------------------------
    # FLUXO PRINCIPAL COM LOOP WHILE
    # ------------------------------------------------------------------
    
    while True:
        # 1. Menu Inicial de Alimentos
        print("\n" + "="*40)
        print("||{:^36}||".format("CARDÁPIO DE ALIMENTOS FEIFOOD"))
        print("="*40)
        
        escolha = input("Digite qual alimento deseja visualizar: ").lower().strip()
        print()
        
        if escolha == "sair":
            print("Saindo do cardápio de alimentos...")
            return # Sai da função, encerrando o cardápio

        # ------------------------------------------------------------------
        # BLOCO DE PIZZA
        # ------------------------------------------------------------------
        if escolha == "pizza":
            print("=="*20)
            print("| !! PIZZAS DISPONÍVEIS !! |")
            print("=="*20)
            
            # Exibe os detalhes
            print("\n[QUEIJO]")
            for chave, valor in queijo.items(): print(f"- {chave} {valor}")
            print("\n[CALABRESA]")
            for chave, valor in calabresa.items(): print(f"- {chave} {valor}")
            print("\n[QUATRO QUEIJOS]")
            for chave, valor in quatro_queijos.items(): print(f"- {chave} {valor}")
            print("\n[FRANGO COM CATUPIRY]")
            for chave, valor in frango_catupiry.items(): print(f"- {chave} {valor}")
            print("=="*20)
            
            # Pergunta de Ação
            while True:
                opcao_pedido = input("Digite 1 para realizar um pedido de PIZZA ou 2 para voltar ao cardápio de alimentos: ").strip()
                if opcao_pedido == "1":
                    # Lógica do pedido
                    escolhasabor = input("Digite o sabor de PIZZA desejado (Ex: QUEIJO): ").lower().strip()
                    print(f"\n✅ Opção '{escolhasabor}' selecionada! Prossiga para o carrinho.")
                    return # Sai da função (e do loop principal)
                elif opcao_pedido == "2":
                    break # Volta ao início do loop principal (escolher PIZZA, HAMBURGUER, etc.)
                else:
                    print("Opção inválida. Digite apenas 1 ou 2.")

        # ------------------------------------------------------------------
        # BLOCO DE HAMBÚRGUER
        # ------------------------------------------------------------------
        elif escolha == "hamburguer":
            print("=="*20)
            print("| !! HAMBÚRGUERES DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes
            print("\n[TRADICIONAL]")
            for chave, valor in tradicional.items(): print(f"- {chave} {valor}")
            print("\n[BACON]")
            for chave, valor in bacon.items(): print(f"- {chave} {valor}")
            print("\n[DUPLO]")
            for chave, valor in duplo.items(): print(f"- {chave} {valor}")
            print("=="*20)
            
            # Pergunta de Ação
            while True:
                opcao_pedido = input("Digite 1 para realizar um pedido de HAMBÚRGUER ou 2 para voltar ao cardápio de alimentos: ").strip()
                if opcao_pedido == "1":
                    # Lógica do pedido
                    escolhasabor = input("Digite o sabor de HAMBÚRGUER desejado (Ex: BACON): ").lower().strip()
                    print(f"\n✅ Opção '{escolhasabor}' selecionada! Prossiga para o carrinho.")
                    return # Sai da função
                elif opcao_pedido == "2":
                    break # Volta ao início do loop principal
                else:
                    print("Opção inválida. Digite apenas 1 ou 2.")

        # ------------------------------------------------------------------
        # BLOCO DE MARMITA
        # ------------------------------------------------------------------
        elif escolha == "marmita":
            print("=="*20)
            print("| !! MARMITAS DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes
            print("\n[FRANGO]")
            for chave, valor in frango_marmita.items(): print(f"- {chave} {valor}")
            print("\n[TILÁPIA]")
            for chave, valor in tilapia.items(): print(f"- {chave} {valor}")
            print("\n[CARNE BOVINA]")
            for chave, valor in carne_bovina.items(): print(f"- {chave} {valor}")
            print("=="*20)
            
            # Pergunta de Ação
            while True:
                opcao_pedido = input("Digite 1 para realizar um pedido de MARMITA ou 2 para voltar ao cardápio de alimentos: ").strip()
                if opcao_pedido == "1":
                    # Lógica do pedido
                    escolhasabor = input("Digite o sabor de MARMITA desejado (Ex: TILÁPIA): ").lower().strip()
                    print(f"\n✅ Opção '{escolhasabor}' selecionada! Prossiga para o carrinho.")
                    return # Sai da função
                elif opcao_pedido == "2":
                    break # Volta ao início do loop principal
                else:
                    print("Opção inválida. Digite apenas 1 ou 2.")

        # ------------------------------------------------------------------
        # OPÇÃO INVÁLIDA DE ALIMENTO PRINCIPAL
        # ------------------------------------------------------------------
        else:
            print("Alimento principal não encontrado. Tente novamente.")
            # O loop "while True" garante que ele tente novamente sem recursão.


# Exemplo de chamada
alimentos()


# def cad_pedidos():
#     # A lista agora armazenará dicionários: [{'item': 'nome', 'quantidade': 'qtd'}, ...]
#     pedidos = []

#     print("\n--- CADASTRO DE PEDIDOS ---")
    
#     while True:
#         # Pede o nome do alimento e sanitiza a entrada
#         pedido_nome = input("Digite o nome do alimento que deseja pedir (ou 'SAIR' para encerrar): ").strip()
        
#         if pedido_nome.lower() == 'sair':
#             break

#         # Pede a quantidade
#         # Adicionei um loop try/except para garantir que a quantidade seja um número inteiro
#         while True:
#             quantidade_str = input(f"Digite a quantidade desejada de '{pedido_nome}': ").strip()
            
#             # Verifica se a string contém apenas dígitos e não está vazia
#             if quantidade_str.isdigit():
#                 # Se for um dígito válido, converte para inteiro
#                 quantidade = int(quantidade_str)
                
#                 # Verifica se a quantidade é positiva
#                 if quantidade > 0:
#                     break  # Sai do loop de quantidade se for válido e positivo
#                 else:
#                     print("A quantidade deve ser maior que zero.")
#             else:
#                 # Se não for um dígito (ex: 'a', '2.5', ' '), é uma entrada inválida.
#                 print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")
        
#         # Armazena o pedido como um dicionário
#         novo_pedido = {
#             "item": pedido_nome, 
#             "quantidade": quantidade
#         }

#         # Armazena o novo pedido como na lista de pedidos
#         pedidos.append(novo_pedido)
        
#         print(f"Pedido '{pedido_nome}' ({quantidade} porção/ões) adicionado com sucesso!")

#         adicionar = input("Deseja adicionar outro pedido? (S/N): ").strip().lower()
#         if adicionar != 's':
#             break
        
#     print("\n------------------------------------------")
#     print("Resumo dos pedidos realizados:")
    
#     # -----------------------------------------------------------
#     # Correção para exibir o formato "item - quantidade porções"
#     # -----------------------------------------------------------
#     if pedidos:
#         for idx, item_pedido in enumerate(pedidos, start=1):
#             # Acessa as chaves "item" e "quantidade" do dicionário
#             nome = item_pedido['item']
#             qtd = item_pedido['quantidade']
            
#             # Formata a saída
#             print(f"  {idx}. {nome} - {qtd} porção(ões)")
#     else:
#         print("Nenhum pedido foi realizado.")

#     print("------------------------------------------")
    
#     return pedidos

def cad_pedidos():
    # A lista armazena dicionários
    pedidos = []
    
    print("\n--- CADASTRO DE PEDIDOS ---")
    
    # Loop de adição de itens
    while True:
        pedido_nome = input("Digite o nome do alimento que deseja pedir (ou 'SAIR' para finalizar): ").strip()
        
        #sai do loop
        if pedido_nome.lower() == 'sair':
            break 

        # Loop de validação de quantidade
        while True:
            quantidade_str = input(f"Digite a quantidade desejada de '{pedido_nome}': ").strip()
            
            if quantidade_str.isdigit():
                quantidade = int(quantidade_str)
                
                #sai do loop
                if quantidade > 0:
                    break
                else:
                    print("A quantidade deve ser maior que zero.")
            else:
                print("Entrada inválida. Digite um número inteiro para a quantidade.")
        
        # Armazena o pedido como um dicionário
        novo_pedido = {
            "item": pedido_nome, 
            "quantidade": quantidade
        }

        # Armazena o novo pedido na lista de pedidos
        pedidos.append(novo_pedido)
        
        print(f"Pedido '{pedido_nome}' ({quantidade} porção/ões) adicionado com sucesso!")

        adc = input("Deseja adicionar outro item? (Sim ou Não): ").strip().lower()
        if adc != 'sim':
            break

    # Se a lista de pedidos estiver vazia, encerra a função
    if len(pedidos) == 0:
        print("Nenhum item foi adicionado ao pedido. Retornando ao Menu...")
        return [] # Retorna lista vazia

    # Endereço de entrega
    print("\n--- ENDEREÇO DE ENTREGA ---")
    endereco = input("Por favor, digite o endereço para entrega: ").strip()
    
    # 3. Confirmar, Editar ou Cancelar
    while True:
        print("\n------------------------------------------")
        print("Resumo do Pedido:")
        exibir_pedidos(pedidos)
        print(f"Endereço de Entrega: {endereco}")
        print("------------------------------------------")

        print("Opções Finais:")
        print("1. Confirmar pedido")
        print("2. Editar pedido")
        print("3. Cancelar pedido")

        print()
        
        opcao_final = input("Digite a opção desejada (1, 2 ou 3): ").strip()

        if opcao_final == '1':
            print("\nPEDIDO CONFIRMADO!")
            print(f"Seu pedido será entregue em: {endereco}")
            # Retorna os dados para que possam ser usados/salvos no sistema
            return {"pedidos": pedidos, "endereco": endereco}

        elif opcao_final == '2':
            # Chama a função de edição
            pedidos = editar_pedido(pedidos)
            # Verifica se a lista ficou vazia após a edição 
            if len(pedidos) == 0: 
                print("\nTodos os itens foram removidos. Pedido cancelado.")
                return [] # Retorna lista vazia p/ cancelamento

        elif opcao_final == '3':
            print("\nSEU PEDIDO FOI CANCELADO.")
            return [] # Retorna lista vazia p/ cancelamento

        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")


# Edição ou exibir
def exibir_pedidos(pedidos_list):
    # Exibe a lista de pedidos 
    if len(pedidos_list) == 0: 
        print("Nenhum item no pedido")
        return
        
    for num, item_pedido in enumerate(pedidos_list, start=1):
        nome = item_pedido['item']
        qtd = item_pedido['quantidade']
        print(f"  {num}. {nome} - {qtd} porção(ões)")


def editar_pedido(pedidos):
    # Permite adicionar ou remover itens do pedido
    
    while True:
        print("\n--- OPÇÕES DE EDIÇÃO ---")
        print("1. Adicionar itens")
        print("2. Remover um item")
        print("3. Voltar ao menu principal do pedido")
        
        opcao_edicao = input("Digite sua opção (1, 2 ou 3): ").strip()

        if opcao_edicao == '1':
            print("\n--- Adicionar Mais Itens ---")
            # Chama a função p/ adicionar itens
            pedidos_adicionais = cad_pedidos_adicionar()
            pedidos.extend(pedidos_adicionais)
            
            # Se adicionou algo, retorna para o menu final
            if len(pedidos_adicionais) > 0:
                return pedidos
            
        elif opcao_edicao == '2':
            # Chama a função p/ remover itens
            pedidos = remover_item(pedidos)
            if len(pedidos) == 0: 
                return []
            
        elif opcao_edicao == '3':
            return pedidos # Volta ao menu final 

        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")
            
        # Loop de edição continua até o usuário escolher a opção '3'
        if opcao_edicao != '1':
             # Mostra o pedido atual após a remoção ou opção inválida
             print("\nPedido atualizado:")
             exibir_pedidos(pedidos)
             
             return pedidos


def cad_pedidos_adicionar():
    # Função de adição de itens.
    pedidos_adicionais = []
    while True:
        pedido_nome = input("Digite o nome do alimento que deseja adicionar (ou 'SAIR'): ").strip()
        
        if pedido_nome.lower() == 'sair':
            break

        while True:
            quantidade_str = input(f"Digite a quantidade desejada de '{pedido_nome}': ").strip()
            
            if quantidade_str.isdigit():
                quantidade = int(quantidade_str)
                if quantidade > 0:
                    break
                else:
                    print("A quantidade deve ser maior que zero.")
            else:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        
        novo_pedido = {"item": pedido_nome, "quantidade": quantidade}
        pedidos_adicionais.append(novo_pedido)
        print(f"Item '{pedido_nome}' ({quantidade} porção/ões) adicionado.")

        adc = input("Deseja adicionar mais algum item? (S/N): ").strip().lower()
        if adc != 's':
            break
            
    return pedidos_adicionais


def remover_item(pedidos):
    # Remove um item com base no indice do pedido

    # Se não houver itens no pedido, não tem nada para remover
    if len(pedidos) == 0: 
        print("Não há itens para remover.")
        return []

    print("\n--- ITENS PARA REMOÇÃO ---")
    exibir_pedidos(pedidos)
    
    while True:
        # Pede o índice do item a ser removido
        indice_str = input(f"Digite o número do item que deseja remover (1 a {len(pedidos)}) ou '0' para cancelar: ").strip()
        
        if indice_str == '0':
            print("Remoção cancelada.")
            return pedidos
        
        if indice_str.isdigit():
            indice = int(indice_str)
            
            # Ajusta o índice para a lista
            lista_indice = indice - 1 
            
            if (lista_indice >= 0) and (lista_indice < len(pedidos)):
                item_removido = pedidos.pop(lista_indice) # Remove e pega o item
                print(f"Item removido: {item_removido['item']} - {item_removido['quantidade']} porção(ões).")
                
                if len(pedidos) == 0: 
                    print("A lista de pedidos está vazia.")
                    return []
                
                return pedidos
            else:
                print(f"Número inválido. Digite um número entre 1 e {len(pedidos)}.")
        else:
            print("Entrada inválida. Por favor, digite um número.")
            
        return pedidos
    
cad_pedidos()



# from tkinter import *

# janela = Tk()
# janela.title("Algoritmos")
# janela.geometry('500x400')

# #cria um rotulo na janela, adiciona um texto e configura fonte
# rotulo = Label(janela, text="Olá, Seja Bem-Vindo ao FEIFOOD!! \n Desejamos que você tenha uma ótima experiência.", font=("Arial Bold", 14), background="lightblue", foreground="black")

# #configura onde a label vai aparecer na janela

# rotulo.place(x=250, y=200, anchor=CENTER)

# janela.mainloop()