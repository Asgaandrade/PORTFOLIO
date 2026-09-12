#Isso é um comentário, vai me ajudar a me organizar e a me orientar ao longo do desenvolvimento do projeto.

#Vou tentar criar um sistema de criação cadastros e teste de login usando python, para práticar a linguagem e lógica.

from time import sleep #método para controle de fluxo.
import metodosLog as mL #Biblioteca local com às funções necessárias para o sistema de login.

#Controle de fluxo condicional(do loop principal):
rodando_prog = True

#Loop principal do programa:
while rodando_prog == True:

    #Interface inicial via treminal e manual básico:
    print("\n[BEM-VINDO(A) AO SISTEMA DE CADASTRO E TESTE DE USUÁRIO DA AA]")
    print("\nManual de uso do sistema")
    print("1 - Sempre cadastre usuários antes de acessá-los;")
    print("2 - Usuários não cadastrados não são localizados, portanto acesso negado;")
    print("3 - O programa roda em loop, então para encerra-lo volte ao menu inicial;")

    #Função de encerrar programa:
    rodando_prog = mL.encerrar_prog()

    #Condicional para parar o programa:
    if rodando_prog == False:
        break

    #Cadastro de usuários:
    banco_de_usuarios = mL.cadastra_user()
    print("\nUsuários Cadastrados:")
    for u in banco_de_usuarios: #Exibindo cada usuário que foi cadastrado.
        print(u[0]+":",u[1])

    #----------------------------------------------------------------------------------

    #Login de usuário:
    user_log = mL.login_user()

    #----------------------------------------------------------------------------------

    #Verificação de acesso:
    acesso_ident = mL.identifica_user(user_log, banco_de_usuarios)

    #----------------------------------------------------------------------------------

    #Informa se o login foi realizado com sucesso ou não:
    mL.registro_print(acesso_ident, user_log)

    #Loop de verificação para testar outros registros:
    teste_reg = True

    while teste_reg == True:

        list_posi = ["sim", "s"]
        list_nega = ["não", "nao", "n"]

        decision = str(input("\nDeseja continuar testando outros registros? [sim/não] "))
        decision_low = decision.lower()

        if decision_low in list_posi: 

            user_log = mL.login_user()
            acesso_ident = mL.identifica_user(user_log, banco_de_usuarios)
            mL.registro_print(acesso_ident, user_log)

        elif decision_low in list_nega:

            print("\nPROGRAMA SENDO REINICIADO [AGUARDE] ... [EXCLUINDO REGISTROS]")
            sleep(2)

            teste_reg = False


    #----------------------------------------------------------------------------------
