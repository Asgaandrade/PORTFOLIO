
#Biblioteca de métodos que criei para usar no sistema de teste de criação de logins:

from time import sleep

#---------------------------------------------------------------------------------

#Função para encerrar o programa:

def encerrar_prog():

    list_posi = ["sim", "s"]
    list_nega = ["não", "nao", "n"]
    loop_valid = True

    while loop_valid == True:
            
        response = str(input("\nDeseja encerrar o programa? [sim/não] "))
        response_low = response.lower()

        if response_low in list_posi: 

            print("[PROGRAMA SENDO ENCERRADO]...")
            sleep(2) #Da biblioteca time
            print("[PROGRAMA ENCERRADO]")
            sleep(2)
            val_encerra = False
            loop_valid = False

        elif response_low in list_nega: 

            val_encerra = True
            loop_valid = False

        elif response_low not in list_posi and response_low not in list_nega: 

            loop_valid = True
            print("\n[ENTRADA INVÁLIDA]")
            print("Digite uma entrada válida! [sim/não]")

    return val_encerra

#---------------------------------------------------------------------------------

#Função para cadastrar usuários:
def cadastra_user():

    cont_users = int(input("\nDigite o número de usuários que deseja cadastrar: "))
    contador = 0
    users_sistem = []
    index = 1

    while contador < cont_users:
        user_cadast = input("\nCrie seu usuário: ")
        password_cadast = input("Crie uma senha de usuário: ")
        tupla_cadast = (str(index), user_cadast, password_cadast)
        index = index + 1
        users_sistem.append(tupla_cadast)
        contador = contador + 1

    return users_sistem

#----------------------------------------------------------------------------------

#Função de login de usuários:
def login_user():
    user_login = input("\nDigite seu nome de usuário: ")
    password_login = input("Digite sua senha de usuário: ")
    tupla_login = (user_login, password_login)

    return tupla_login

#--------------------------------------------------------------------------------

#Função para verificar se o login e senha coincidem com um registro(tupla) na lista de usuários:
def identifica_user(usuario_senha, usuarios_sistema):

    #Verificacao de tupla(user e senha):
    for tupla_reg in usuarios_sistema: 
        if tupla_reg[1:] == usuario_senha: #Tupla (index, user, senha), porém está verificando apenas  se a tupla (user, senha) é igual alguma 
            retorno_login = True
            break
        else:
            retorno_login = False

    return retorno_login

#----------------------------------------------------------------------------------

def registro_print(perm_acesso, user):
        
    #Validando login:
        if perm_acesso == True:
            print("\nAcesso liberado!")
            print(f"Seu registro está funcionando, bem vindo {user[0]}.\n")
    
        elif perm_acesso == False:
            print("\nAcesso negado!")
            print("Credenciais não localizadas!")
            print("\nSe desejar, cadastre seu usuário.")

#----------------------------------------------------------------------------------