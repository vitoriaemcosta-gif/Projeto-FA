# def verificar(entrar) :
#     if entrar == 1:
#         menu()
#     elif entrar == 0:
#         login()

# def usuario() :
#     cadastro = []
#     login = []
#     print("Seja Bem vindo(a) ao FEIFOOD !!! ")
#     user = int(input("• Digite 1 para realizar o seu cadastro ou 2 para realizar login: "))

#     if user == 1:
#         cadnm = input("Digite seu nome: ")
#         cadtl = int(input("Digite seu telefone: "))
#         cadem = input("Digite seu email: ")
#         cadsn = input("Digite sua senha (com até 5 letras) : ")
    
#         cadastro.append(cadnm)    
#         cadastro.append(cadtl)  
#         cadastro.append(cadem)  
#         cadastro.append(cadsn)  
#         login.append(cadem)
#         login.append(cadsn)

#         if user == 2:
#             verificar(login())

    

#     print(cadastro)
#     print(login)

# def login():

#         loginem = input("Digite seu email: ")
#         loginsn = input("Digite sua senha: ")

#         for i in range(0, len(login),2):

#             if loginem == login[i] and loginsn == login[i+1] :
#                 verificar = 1

#             else:
#                 verificar = 0
            
#             return verificar

# usuario()

# def menu() :
#     print ("MENU:\n • Buscar alimentos \n • Cadastrar pedido \n • Avaliar pedido  ")
#     area = int(input("Digite qual área você deseja acessar: "))

#     if area == "Buscar alimentos":
#         alimentos()

#     elif area == "Cadastrar pedido":
#         cad_pedidos()

#     elif area == "Avaliar pedido":
#         avaliar()

#     else:
#         print("Opção inválida !!!!!")


def alimentos ():
    pizza = { 'Sabores: ': 'Queijo ou Calabresa'}

    queijo = {'Descrição: ' : 'Clássica pizza de massa fina ou grossa, coberta com molho de tomate e generosa camada de queijo mussarela;',
              'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas;',
              'Valor: ' : 'R$60,00'}
    
    calabresa = {'Descrição: ' : 'Pizza tradicional com molho de tomate, queijo mussarela, fatias de linguiça calabresa e cebola;',
                 'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas.',
                 'Valor: ' : 'R$65,00'}
    
    hamburguer = {'Sabores: ' : 'tradicional ou bacon'}

    tradicional = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina e queijo mussarela ou prato, salada de alface e tomate;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$22,00'}
    
    bacon = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo e fatias de bacon crocante;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}
    
    
    marmitas = {'Sabores: ' : 'Frango ou Tilápia.'}

    frango = {'Descrição: ' : 'Marmita com filé de peito de frango grelhado, acompanhado de arroz, feijão e batata frita;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}
    
    tilapia = {'Descrição: ' : 'Marmita com filé de peixe Tilápia grelhado, assado ou frito, acompanhado de arroz e salada;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}
    
    sushi = {'Descrição: ' : 'Prato da culinária japonesa. Combo com diferentes tipos de sushis (uramaki, niguiri, hossomaki) e um Temaki (cone de alga recheado com salmão);',
                 'Porção: ' : '1 pessoa (15 peças);',
                 'Valor: ' : 'R$50,00'}
    
    escolha = input("Digite qual alimento deseja vizualizar: ").upper()
    print()

    if escolha == "PIZZA":
        for sabores, descricao  in pizza.items() :
            print(sabores, descricao)
            print()

            escolhasabor = input("Digite o sabor desejado ou 'voltar' para retornar ao cardapio de alimentos: ").upper()
            print()

            if escolhasabor == "QUEIJO":
                print("\n| !! PIZZA DE QUEIJO !! |")
                print()
                for sabores, descricao  in queijo.items() :
                    print(sabores, descricao)
                    print()

            if escolhasabor == "CALABRESA":
                print("\n| !! PIZZA DE CALABRESA !! |")
                print()
                for sabores, descricao  in calabresa.items() :
                    print(sabores, descricao)
                    print()

            elif escolhasabor == "VOLTAR":
                alimentos()

            else:
                print("Opção inválida!!!")
                #criar função para voltar para a questão

        
    if escolha == "HAMBURGUER":
        for sabores, descricao  in hamburguer.items() :
            print(sabores, descricao)
            print()

            escolhasabor = input("Digite o sabor desejado ou 'voltar' para retornar ao cardápio de alimentos: ").upper()
            print()

            if escolhasabor == "TRADICIONAL":
                print("\n| !! HAMBURGUER TRADICIONAL !! |")
                print()
                for sabores, descricao  in tradicional.items() :
                    print(sabores, descricao)
                    print()

            if escolhasabor == "BACON":
                print("\n| !! HAMBURGUER COM BACON !! |")
                print()
                for sabores, descricao  in bacon.items() :
                    print(sabores, descricao)
                    print()

            elif escolhasabor == "VOLTAR":
                alimentos()

            else:
                print("Opção inválida!!!")
                #criar função para voltar para a questão

    if escolha == "MARMITA":
        for sabores, descricao  in marmitas.items() :
            print(sabores, descricao)
            print()

            escolhasabor = input("Digite o sabor desejado ou 'voltar' para retornar ao cardápio de alimentos: ").upper()
            print()

            if escolhasabor == "FRANGO":
                print("\n| !! MARMITA DE FRANGO !! |")
                print()
                for sabores, descricao  in frango.items() :
                    print(sabores, descricao)
                    print()

            if escolhasabor == "TILÁPIA":
                print("\n| !! MARMITA DE TILÁPIA !! |")
                print()
                for sabores, descricao  in tilapia.items() :
                    print(sabores, descricao)
                    print()

            elif escolhasabor == "VOLTAR":
                alimentos()

            else:
                print("Opção inválida!!!")
                #criar função para voltar para a questão

    
alimentos()



# def cad_pedidos():


# def avaliar():



    


   

    

