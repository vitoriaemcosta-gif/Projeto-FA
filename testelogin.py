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
        
        escolha = input("Digite qual alimento deseja visualizar: ").upper().strip()
        print()
        
        if escolha == "SAIR":
            print("Saindo do cardápio de alimentos...")
            return # Sai da função, encerrando o cardápio

        # ------------------------------------------------------------------
        # BLOCO DE PIZZA
        # ------------------------------------------------------------------
        if escolha == "PIZZA":
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
                    escolhasabor = input("Digite o sabor de PIZZA desejado (Ex: QUEIJO): ").upper().strip()
                    print(f"\n✅ Opção '{escolhasabor}' selecionada! Prossiga para o carrinho.")
                    return # Sai da função (e do loop principal)
                elif opcao_pedido == "2":
                    break # Volta ao início do loop principal (escolher PIZZA, HAMBURGUER, etc.)
                else:
                    print("Opção inválida. Digite apenas 1 ou 2.")

        # ------------------------------------------------------------------
        # BLOCO DE HAMBÚRGUER
        # ------------------------------------------------------------------
        elif escolha == "HAMBURGUER":
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
                    escolhasabor = input("Digite o sabor de HAMBÚRGUER desejado (Ex: BACON): ").upper().strip()
                    print(f"\n✅ Opção '{escolhasabor}' selecionada! Prossiga para o carrinho.")
                    return # Sai da função
                elif opcao_pedido == "2":
                    break # Volta ao início do loop principal
                else:
                    print("Opção inválida. Digite apenas 1 ou 2.")

        # ------------------------------------------------------------------
        # BLOCO DE MARMITA
        # ------------------------------------------------------------------
        elif escolha == "MARMITA":
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
                    escolhasabor = input("Digite o sabor de MARMITA desejado (Ex: TILÁPIA): ").upper().strip()
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