# Lista global para armazenar as credenciais (email e senha).
cad_dados = []
login_dados = []

cardapio_precos = {
    # Pizzas
    "pizza de queijo": 60.00,
    "pizza de calabresa": 65.00,
    "pizza de quatro queijos": 68.00,
    "pizza de frango com catupiry": 70.00,

    # Hamburgueres
    "hamburguer tradicional": 22.00,
    "hamburguer bacon": 27.00,
    "hamburguer duplo": 35.00,

    # Marmitas
    "marmita de frango": 27.00,
    "marmita de tilapia": 27.00,
    "marmita de carne bovina": 32.00,

    # Doces
    "brigadeiro": 5.00,
    "pudim": 15.00,
    "bolo de pote": 18.00,
    "fatia de torta": 20.00,

    # Bebidas
    "refrigerante de lata": 7.00,
    "suco natural": 10.00,
    "água mineral": 4.00,

}

# Funções de pedido

def exibir_pedidos(pedidos_list):
    # Exibe a lista de pedidos
    if len(pedidos_list) == 0:
        print("Nenhum item no pedido")
        return

    for num, item_pedido in enumerate(pedidos_list, start=1):
        nome = item_pedido['item']
        qtd = item_pedido['quantidade']
        print(f"  {num}. {nome} - {qtd} porção(ões)")


def cad_pedidos_adicionar():
    # Função de adição de itens
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
        

def calcular_preco_total(pedidos_list):
    # Usamos o dicionário global de preços
    global cardapio_precos 
    
    total = 0.0
    
    # Lista para itens com preço não encontrado (fora do cardápio)
    itens_nao_encontrados = []
    
    for item_pedido in pedidos_list:
        nome_item = item_pedido['item'].lower() 
        quantidade = item_pedido['quantidade']
        
        # Verifica se o item está no cardápio de preços
        if nome_item in cardapio_precos:
            preco_unitario = cardapio_precos[nome_item]
            subtotal = preco_unitario * quantidade
            total += subtotal
        else:
            # Adiciona o item à lista de não encontrados, pois o preço não está no cardapio_precos
            itens_nao_encontrados.append(item_pedido['item'])

    return total, itens_nao_encontrados

# Funções principais 

def alimentos():
    # Pizzas
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

    # Hamburgueres
    tradicional = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo, alface e tomate;',
                   'Porção: ' : '1 pessoa;',
                   'Valor: ' : 'R$22,00'}
    bacon = {'Descrição: ' : 'Sanduíche com pão, hambúrguer de carne bovina, queijo e fatias de bacon crocante;',
             'Porção: ' : '1 pessoa;',
             'Valor: ' : 'R$27,00'}
    duplo = {'Descrição: ' : 'Pão, dois hambúrgueres de 150g, queijo cheddar e molho especial.',
             'Porção: ' : '1 pessoa;',
             'Valor: ' : 'R$35,00'}

    # Marmitas
    frango_marmita = {'Descrição: ' : 'Marmita com filé de peito de frango grelhado, acompanhado de arroz, feijão e batata frita;',
                      'Porção: ' : '1 pessoa;',
                      'Valor: ' : 'R$27,00'}
    tilapia = {'Descrição: ' : 'Marmita com filé de peixe Tilápia grelhado, assado ou frito, acompanhado de arroz e salada;',
               'Porção: ' : '1 pessoa;',
               'Valor: ' : 'R$27,00'}
    carne_bovina = {'Descrição: ' : 'Marmita com Bife Acebolado, acompanhado de arroz, feijão, farofa e couve refogada.',
                    'Porção: ' : '1 pessoa;',
                    'Valor: ' : 'R$32,00'}
    
    # Doces
    brigadeiro = {'Descrição: ' : 'Clássico brigadeiro gourmet, feito com chocolate belga.',
                  'Porção: ' : 'Unidade (aprox. 30g);',
                  'Valor: ' : 'R$5,00'}
    pudim = {'Descrição: ' : 'Pudim de leite condensado com calda de caramelo caseira.',
             'Porção: ' : 'Fatia individual;',
             'Valor: ' : 'R$15,00'}
    bolo_de_pote = {'Descrição: ' : 'Bolo de chocolate com recheio cremoso em camadas.',
                    'Porção: ' : '250ml;',
                    'Valor: ' : 'R$18,00'}
    torta_fatia = {'Descrição: ' : 'Fatia de torta holandesa.',
                   'Porção: ' : 'Fatia;',
                   'Valor: ' : 'R$20,00'}
    
    # Bebidas
    refrigerante_lata = {'Descrição: ' : 'Diversas opções de refrigerantes em lata (Coca, Guaraná, Soda).',
                         'Porção: ' : 'Lata 350ml;',
                         'Valor: ' : 'R$7,00'}
    suco_natural = {'Descrição: ' : 'Sabores variados de suco feito na hora (Laranja, Morango, Limão).',
                    'Porção: ' : 'Copo 500ml;',
                    'Valor: ' : 'R$10,00'}
    agua_mineral = {'Descrição: ' : 'Água mineral sem gás.',
                    'Porção: ' : 'Garrafa 500ml;',
                    'Valor: ' : 'R$4,00'}

    while True:
        # Menu Inicial de Alimentos
        print("\n" + "="*40)
        print("||{:^36}||".format("CARDÁPIO DE ALIMENTOS FEIFOOD"))
        print("="*40) 
        print()
        print("="*20)
        print(" 1 - Pizza")
        print("="*20)
        print(" 2 - Hamburguer")
        print("="*20)
        print(" 3-  Marmita")
        print("="*20)
        print(" 4-  Doces")
        print("="*20)
        print(" 5-  Bebidas")

        print()

        escolha = input("Digite qual opção deseja visualizar (1, 2, 3, 4 ou 5)\n(ou 'sair' para voltar ao menu): ").lower().strip()
        print()

        if escolha == "sair":
            print("Saindo do cardápio de alimentos...")
            return # Sai da função, encerrando o cardápio


        # Pizza
        if escolha in ("1", "pizza"):
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
            print()
            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio


        # Hamburguer
        elif escolha in ("2", "hamburguer"):
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
            print()
            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio


        # Marmita
        elif escolha in ("3", "marmita"):
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
            print()
            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio
            
        elif escolha in ("4", "doces"):
            print("=="*20)
            print("| !! DOCES DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes dos doces
            print("\n[BRIGADEIRO]")
            for chave, valor in brigadeiro.items(): 
                print(f"- {chave} {valor}")

            print("\n[PUDIM]")
            for chave, valor in pudim.items(): 
                print(f"- {chave} {valor}")

            print("\n[BOLO DE POTE]")
            for chave, valor in bolo_de_pote.items(): 
                print(f"- {chave} {valor}")
                
            print("\n[FATIA DE TORTA]")
            for chave, valor in torta_fatia.items(): 
                print(f"- {chave} {valor}")
            print()
            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função, encerrando o cardápio

        # Bebidas
        elif escolha in ("5", "bebidas"):
            print("=="*20)
            print("| !! BEBIDAS DISPONÍVEIS !! |")
            print("=="*20)

            # Exibe os detalhes das bebidas
            print("\n[REFRIGERANTE DE LATA]")
            for chave, valor in refrigerante_lata.items(): 
                print(f"- {chave} {valor}")

            print("\n[SUCO NATURAL]")
            for chave, valor in suco_natural.items(): 
                print(f"- {chave} {valor}")

            print("\n[ÁGUA MINERAL]")
            for chave, valor in agua_mineral.items(): 
                print(f"- {chave} {valor}")
            print()
            print("=="*20)

            voltar = input("Deseja voltar ao menu de alimentos? (Sim ou Não): ").strip().lower()
            if voltar != 'sim':
                print("Saindo do cardápio de alimentos...")
                return # Sai da função do cardapio
            
        #opção invalida
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
    print()

    # 3. Confirmar, Editar ou Cancelar
    while True:
        print("=="*20)
        print("\nResumo do Pedido:")
        print()
        exibir_pedidos(pedidos)
        print(f"Endereço de Entrega: {endereco}")
        print("=="*20)

        print("Opções Finais:")
        print("1. Confirmar pedido")
        print("2. Editar pedido")
        print("3. Cancelar pedido")

        print()

        opcao_final = input("Digite a opção desejada (1, 2 ou 3): ").strip()

        if opcao_final == '1':
            # Calcula o preço total e lista de itens não encontrados
            preco_total, itens_nao_encontrados = calcular_preco_total(pedidos)
            
            print("\nPEDIDO CONFIRMADO!")
            print("Resumo Final do Pedido:")
            exibir_pedidos(pedidos)
            print()
            print(f"VALOR TOTAL: R${preco_total:.2f}") 
            print()
            print(f"Seu pedido será entregue em: {endereco}")

            if itens_nao_encontrados:
                # Exibe alerta para itens sem preço no cardápio
                print("Informamos que os seguintes itens não foram contabilizados, pois não foram encontrados no nosso cardápio de preços:")
                
                for item in itens_nao_encontrados:
                    print(f"- {item}")

            
            # Retorna os dados para que possam ser usados/salvos no sistema
            return {"pedidos": pedidos, "endereco": endereco, "total": preco_total}

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


def avaliar():

    # Solicita e processa a avaliação do último pedido do usuário (de 1 a 5 estrelas).

    print("=="*20)
    print(" Avalie seu último pedido!")
    print("=="*20)

    # Loop para garantir que a entrada seja válida
    while True:
        # Pede a entrada como string
        avaliacao_str = input("Por favor, avalie seu pedido de 1 a 5 estrelas: ").strip()
        
        # Verifica se a entrada é um número inteiro
        if avaliacao_str.isdigit():
            avaliacao = int(avaliacao_str)
            
            # Verifica se o número está dentro do intervalo permitido (1 a 5)
            if 1 <= avaliacao <= 5:
                # Se for válida, sai do loop
                break
            else:
                # Se for um número, mas estiver fora do intervalo
                print("Opção inválida!!! Digite um número inteiro entre 1 e 5.")
        else:
            # Se não for um número
            print("Entrada inválida. Por favor, digite um número inteiro.")

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

    print("Agradedemos pela sua avaliação !!!")
    print("=="*20)
    print()


def menu() :
    while True:

        print ("\n=== MENU PRINCIPAL FEIFOOD ===\n")
        print (" • 1 - Buscar alimentos \n • 2 - Cadastrar pedido \n • 3 - Avaliar pedido \n • 4 - Sair \n")

        area = input("Digite qual área você deseja acessar (1, 2, 3 ou 4): ").strip()
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
            print("Opção inválida !!!!! Digite apenas 1, 2, 3 ou 4.")


# --- FUNÇÕES DE AUTENTICAÇÃO ---

def verificar(entrar) :
    if entrar == 1:
        # Quando o login é bem-sucedido, chama o menu.
        print("\nLogin bem-sucedido!")
        menu()
        print() # Adiciona uma linha em branco após o menu
    elif entrar == 0:
        print("Email ou senha incorretos. Tente novamente.")
        login_result = login() # Tenta o login novamente
        verificar(login_result) # Verifica o resultado do novo login


def login():
    global login_dados

    # Se não houver dados cadastrados, impede o login
    if not login_dados:
            # RETORNA AQUI PARA EVITAR O BUG
            print("\nNenhum usuário cadastrado.")
            print("Por favor, execute o programa novamente e escolha a opção de cadastro (1).")
            return
    
    print("\n--- LOGIN DE USUÁRIO ---")
    print()
    loginem = input("Digite seu email: ")
    loginsn = input("Digite sua senha: ")

    # Percorre a lista de credenciais global (email, senha, email, senha, ...)
    for i in range(0, len(login_dados), 2):
        # Compara o email e a senha digitados com os pares na lista
        if loginem == login_dados[i] and loginsn == login_dados[i+1]:
            return 1 # Encontrado: Sucesso

    # Se o loop terminar sem encontrar a credencial
    return 0 # Falha


def usuario() :
    global login_dados # Indica que vamos usar a lista global
    global cad_dados # Indica que vamos usar a lista global

    

    while True:

        print("Seja Bem vindo(a) ao FEIFOOD !!! ")
        print()
        # Pede a entrada como string
        user_input = input("• 1 - Realizar Cadastro \n• 2 - Realizar Login \n\nDigite a opção desejada (1 ou 2): ").strip()

        if user_input in ('1', '2'):
            user = int(user_input) # Converte para inteiro apenas se for válido
            break # Sai do loop
        else:
            print("Opção inválida. Por favor, digite apenas 1 ou 2.")

    if user == 1:
        # Bloco de Cadastro
        cadnm = input("Digite seu nome: ")

        while True:
            cadtl_str = input("Digite seu telefone (apenas números): ")
            if cadtl_str.isdigit():
                cadtl = cadtl_str
                break
            else:
                print("Entrada inválida. Por favor, digite apenas números para o telefone.")
                
        cadem = input("Digite seu email: ")
        cadsn = input("Digite sua senha (com até 5 letras) : ")

        # 1. Salva as credenciais na lista global
        cad_dados.append(cadnm)
        cad_dados.append(cadtl)
        login_dados.append(cadem)
        login_dados.append(cadsn)

        print()
        print("=="*20)
        print("Cadastro realizado com sucesso !!!")
        print("=="*20)
        print()
        print("Faça o login para acessar o FEIFOOD...")


        # Chama o login após o cadastro
        verificar(login())

    elif user == 2:
        # Chama o login se a opção for 2
        verificar(login())


# Chama a função inicial
usuario()