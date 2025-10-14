def verificar(poste) :
    if poste == 1:
        menu()
    elif poste == 0:
        login()

def usuario() :
    cadastro = []
    login = []
    print("Seja Bem vindo(a) ao FEIFOOD !!! ")
    user = int(input("• Digite 1 para realizar o seu cadastro ou 2 para realizar login: "))

    if user == 1:
        cadnm = input("Digite seu nome: ")
        cadtl = int(input("Digite seu telefone: "))
        cadem = input("Digite seu email: ")
        cadsn = input("Digite sua senha (com até 5 letras) : ")
    
        cadastro.append(cadnm)    
        cadastro.append(cadtl)  
        cadastro.append(cadem)  
        cadastro.append(cadsn)  
        login.append(cadem)
        login.append(cadsn)

        if user == 2:
            verificar(login())

    

    print(cadastro)
    print(login)

def login():

        loginem = input("Digite seu email: ")
        loginsn = input("Digite sua senha: ")

        for i in range(0, len(login),2):

            if loginem == login[i] and loginsn == login[i+1] :
                verificar = 1

            else:
                verificar = 0
            
            return verificar

usuario()

def menu() :
    print("oi")
    


   

    

