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


def menu() :
    while True:

        print ("MENU:\n • Buscar alimentos \n • Cadastrar pedido \n • Avaliar pedido \n • Sair \n")
        
        area = input("Digite qual área você deseja acessar: ").upper()
        print()
        if area == "BUSCAR ALIMENTOS":
            alimentos()

        elif area == "CADASTRAR PEDIDO":
            cad_pedidos()

        elif area == "AVALIAR PEDIDO":
            avaliar()
        
        elif area == "SAIR":
            print("Obrigado por usar o FEIFOOD !!!")
            break

        else:
            area = input("Opção inválida !!!!! \nDigite qual área você deseja acessar: ").upper()



def alimentos():

    #Pizas
    pizza = { 'Sabores: ': 'Queijo ou Calabresa'}

    queijo = {'Descrição: ' : 'Clássica pizza de massa fina ou grossa, coberta com molho de tomate e generosa camada de queijo mussarela;',
              'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas;',
              'Valor: ' : 'R$60,00'}
    
    calabresa = {'Descrição: ' : 'Pizza tradicional com molho de tomate, queijo mussarela, fatias de linguiça calabresa e cebola;',
                 'Porção: ' : 'Tamanho Grande (8-10 fatias): 3 a 4 pessoas.',
                 'Valor: ' : 'R$65,00'}
    

    #Hambúrgueres
    hamburguer = {'Sabores: ' : 'tradicional ou bacon'}

    tradicional = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina e queijo mussarela ou prato, salada de alface e tomate;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$22,00'}
    
    bacon = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo e fatias de bacon crocante;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}
    
    #Marmitas
    marmitas = {'Sabores: ' : 'Frango ou Tilápia.'}

    frango = {'Descrição: ' : 'Marmita com filé de peito de frango grelhado, acompanhado de arroz, feijão e batata frita;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}
    
    tilapia = {'Descrição: ' : 'Marmita com filé de peixe Tilápia grelhado, assado ou frito, acompanhado de arroz e salada;',
                 'Porção: ' : '1 pessoa;',
                 'Valor: ' : 'R$27,00'}

    #entrada do alimento
    escolha = input("Digite qual alimento deseja vizualizar: ").upper()
    print()

    #entrada dos sabores de pizza
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
                return

            else:
                #escolhe o sabor novamente
                escolhasabor = input("Opção inválida!!! \nDigite o sabor desejado ou 'voltar' para retornar ao cardapio de alimentos: ").upper()
                

     #entrada dos sabores de hamburgueres 
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

            elif escolhasabor == "BACON":
                print("\n| !! HAMBURGUER COM BACON !! |")
                print()
                for sabores, descricao  in bacon.items() :
                    print(sabores, descricao)
                    print()

            elif escolhasabor == "VOLTAR":
                return

            else:
                #escolhe o sabor novamente
                escolhasabor = input("Opção inválida!!! \nDigite o sabor desejado ou 'voltar' para retornar ao cardapio de alimentos: ").upper()
                

    #entrada dos sabores de marmitas
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

            elif escolhasabor == "TILÁPIA":
                print("\n| !! MARMITA DE TILÁPIA !! |")
                print()
                for sabores, descricao  in tilapia.items() :
                    print(sabores, descricao)
                    print()

            elif escolhasabor == "VOLTAR":
                return

            else:
                #escolhe o sabor novamente
                escolhasabor = input("Opção inválida!!! \nDigite o sabor desejado ou 'voltar' para retornar ao cardapio de alimentos: ").upper()
                



def cad_pedidos():
    print('')

def avaliar():
    """
    Solicita e processa a avaliação do último pedido do usuário (de 1 a 5 estrelas).
    """
    print("------------------------------------------")
    print(" Avalie seu último pedido!")
    print("------------------------------------------")

    # Loop para garantir que a entrada seja válida
    while True:
            # Solicita a nota, convertendo a entrada para número inteiro
            avaliacao = int(input("Por favor, avalie seu pedido de 1 a 5 estrelas: "))
            
            # Verifica se a nota está dentro do intervalo permitido (1 a 5)
            if 1 <= avaliacao <= 5:
                # Se for válida, sai do loop
                break
            else:
                # Se não estiver no intervalo
                print("Opção inválida!!! Digite um número inteiro entre 1 e 5.")
        
    # Mensagens de feedback baseadas na nota
    print("\n------------------------------------------")
    if avaliacao == 5:
        print(f"⭐⭐⭐⭐⭐")
        print("Uau! Obrigado pelo feedback e volte sempre!")
    elif avaliacao == 4:
        print(f"⭐⭐⭐⭐")
        print("Que bom que gostou! Sua nota 4 nos motiva a melhorar ainda mais.")
    elif avaliacao == 3:
        print(f"⭐⭐⭐")
        print("Agradecemos sua nota 3. Estamos trabalhando para que seu próximo pedido seja 5 estrelas.")
    elif avaliacao == 2:
        print(f"⭐⭐")
        print("Recebemos sua nota 2. Sentimos muito pela experiência. Vamos analisar e corrigir o que for necessário.")
    elif avaliacao == 1:
        print(f"⭐")
        print("Sua nota 1 é um alerta para nós. Entraremos em contato para entender o ocorrido e compensar a má experiência.")
        
    print(f"Nota Registrada: {avaliacao} estrelas.")
    print("------------------------------------------")
    print()

menu()
    
# Chama a função para rodar o sistema de avaliação



    


   

    

