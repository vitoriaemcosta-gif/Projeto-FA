# Lista global para armazenar as credenciais (email e senha).
# Mover esta lista para fora das funções é o principal ponto de correção.
cad_dados = []
login_dados = []

cardapio_precos = {
    # Pizzas
    "queijo": 60.00,
    "calabresa": 65.00,
    "quatro queijos": 68.00,
    "frango com catupiry": 70.00,

    # Hamburgueres
    "tradicional": 22.00,
    "bacon": 27.00,
    "duplo": 35.00,

    # Marmitas
    "frango": 27.00,
    "tilapia": 27.00,
    "carne bovina": 32.00
}


def verificar(entrar) :
    if entrar == 1:
        menu()
        print()
    elif entrar == 0:
        print("Email ou senha incorretos. Tente novamente.")
        login()


def usuario() :
    global login_dados # Indica que vamos usar a lista global
    global cad_dados # Indica que vamos usar a lista global

    print("Seja Bem vindo(a) ao FEIFOOD !!! ")
    
    # Substituindo try/except por um loop while para garantir a entrada
    while True:
        # Pede a entrada como string
        user_input = input("• Digite 1 para realizar o seu cadastro ou 2 para realizar login: ")
        
        if user_input in ('1', '2'):
            user = int(user_input) # Converte para inteiro apenas se for válido
            break # Sai do loop
        else:
            print("Opção inválida. Por favor, digite apenas 1 ou 2.")

    if user == 1:
        # Bloco de Cadastro
        cadnm = input("Digite seu nome: ")
        # Atenção: Se o usuário digitar letras aqui, o programa ainda falhará,
        # pois não estamos tratando o erro com try/except.
        cadtl = int(input("Digite seu telefone: ")) 
        cadem = input("Digite seu email: ")
        cadsn = input("Digite sua senha (com até 5 letras) : ")
        
        # 1. Salva as credenciais na lista global
        cad_dados.append(cadnm)    
        cad_dados.append(cadtl)
        login_dados.append(cadem)
        login_dados.append(cadsn)

        print()
        print("Cadastro realizado com sucesso !!!\nFaça o login para acessar o FEIFOOD. \n")
        
        # Chama o login após o cadastro
        verificar(login()) 

    elif user == 2:
        # Chama o login se a opção for 2
        verificar(login())


def login():
    global login_dados

    loginem = input("Digite seu email: ")
    loginsn = input("Digite sua senha: ")

    # Percorre a lista de credenciais global (email, senha, email, senha, ...)
    for i in range(0, len(login_dados), 2):
        # Compara o email e a senha digitados com os pares na lista
        if loginem == login_dados[i] and loginsn == login_dados[i+1]:
            return 1 # Encontrado: Sucesso

    # Se o loop terminar sem encontrar a credencial
    return 0 # Falha

# Chama a função inicial
usuario()

def menu() :
    while True:

        print ("MENU:\n • 1 - Buscar alimentos \n •2 - Cadastrar pedido \n • 3 - Avaliar pedido \n • 4 - Sair \n")
        
        area = input("Digite qual área você deseja acessar (1, 2, 3 ou 4): ").lower()
        print()

        #Condições do menu
        if area == "1":
            alimentos()

        elif area == "2":
            cad_pedidos()

        elif area == "3":
            avaliar()
        
        elif area == "4":
            print("Obrigado por usar o FEIFOOD !!!")
            break

        else:
            area = input("Opção inválida !!!!! \nDigite qual área você deseja acessar (1, 2, 3 ou 4): ").lower()


def alimentos():
    
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


    # FLUXO PRINCIPAL COM LOOP WHILE
    
    while True:
        # 1. Menu Inicial de Alimentos
        print("\n" + "="*40)
        print("||{:^36}||".format("CARDÁPIO DE ALIMENTOS FEIFOOD"))
        print("="*40)
        print("Opções de Alimentos Disponíveis:")
        print("="*40)
        print(" 1 - Pizza") 
        print("="*40)
        print(" 2 - Hamburguer")  
        print("="*40)
        print(" 3-  Marmita")

        print()
        
        escolha = input("Digite qual alimento deseja visualizar (1, 2 ou 3)\n(ou 'sair' para voltar ao menu): ").lower().strip()
        print()
        
        if escolha == "sair":
            print("Saindo do cardápio de alimentos...")
            return # Sai da função, encerrando o cardápio

    
        # Pizza
     
        if escolha == "pizza":
            print("=="*20)
            print("| !! PIZZAS DISPONÍVEIS !! |")
            print("=="*20)
            
            # Exibe os detalhes das pizzas

            print("\n[QUEIJO]")
            for chave, valor in queijo.items(): 
                print(f"- {chave} {valor}")

            print("\n[CALABRESA]")
            for chave, valor in calabresa.items(): 
                print(f"- {chave} {valor}")

            print("\n[QUATRO QUEIJOS]")
            for chave, valor in quatro_queijos.items(): 
                print(f"- {chave} {valor}")

            print("\n[FRANGO COM CATUPIRY]")
            for chave, valor in frango_catupiry.items(): 
                print(f"- {chave} {valor}")

            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio
            

        # Hamburguer

        elif escolha == "hamburguer":
            print("=="*20)
            print("| !! HAMBÚRGUERES DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes dos hambúrgueres

            print("\n[TRADICIONAL]")
            for chave, valor in tradicional.items(): 
                print(f"- {chave} {valor}")

            print("\n[BACON]")
            for chave, valor in bacon.items(): 
                print(f"- {chave} {valor}")

            print("\n[DUPLO]")
            for chave, valor in duplo.items(): 
                print(f"- {chave} {valor}")

            print("=="*20)
            
            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio
         

        # Marmita

        elif escolha == "marmita":
            print("=="*20)
            print("| !! MARMITAS DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes das marmitas

            print("\n[FRANGO]")
            for chave, valor in frango_marmita.items(): 
                print(f"- {chave} {valor}")

            print("\n[TILÁPIA]")
            for chave, valor in tilapia.items(): 
                print(f"- {chave} {valor}")

            print("\n[CARNE BOVINA]")
            for chave, valor in carne_bovina.items(): 
                print(f"- {chave} {valor}")

            print("=="*20)
            
            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio
           
        # Opção inválida
     
        else:
            print("Alimento não encontrado. Tente novamente.")

def cad_pedidos():
    # A lista armazena dicionários
    pedidos = []
    
    print("\n--- CADASTRO DE PEDIDOS ---")
    
    # Loop de adição de itens
    while True:
        pedido_nome = input("Digite o nome do alimento que deseja pedir (ou 'SAIR' para finalizar): ").strip()
        print()

        #sai do loop
        if pedido_nome.lower() == 'sair':
            break 

        # Loop de validação de quantidade
        while True:
            quantidade_str = input(f"Digite a quantidade desejada: ").strip()
            
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
    
# Chama a função para rodar o sistema de avaliação





    


   

    

