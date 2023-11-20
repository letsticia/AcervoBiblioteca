"""Módulo com as funções das telas de menu."""

from formatacao import *

def menuInicial():
    """Cumpre o requisito [RF001] Menu inicial:\n
    O sistema deve conter as opções de 1. login gerente, 2. cadastro funcionário, 3. loginfuncionário.\n 
    PRIORIDADE: ( ) Essencial; ( ) Importante; (X) Desejável.
    """
    nomeMenu("Menu Inicial")
    centralizado("(1)   Logar como Gerente")
    centralizado("(2)   Logar como Funcionário")
    centralizado("(3)   Cadastrar um Funcionário")
    centralizado("(4)   Sair do Arcevo Bibliotecário")

    print("\n" + "="*60 + "\n")
    opcao = input("Selecione uma opção:")
    
    # analisando o input
    if opcao == "1":
        print("\nRedirecionando para a tela de Login de Gerente...\n")
        from logins import loginGerente
        return loginGerente()
    elif opcao == "2":
        print("\nRedirecionando para a tela de Login de Funcionário...\n")
        from logins import loginFuncionario
        return loginFuncionario()
    elif opcao == "3":
        print("\nRedirecionando para a tela de Cadastro de Funcionário...\n")
        from logins import cadastroFuncionario
        return cadastroFuncionario()
    elif opcao == "4":
        print("\nSaindo do arcevo bibliotecário...\n")
        return False
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuInicial()

def menuFuncionario(gerente=bool):
    """Cumpre o requisito [RF008] Menu funcionário:
    Após a entrada do usuário no sistema ele terá um menu com as seguintes opções: cadastrar
    usuário, cadastrar livro, buscar livro, empréstimos, remover livro, remover usuário, logout.
    PRIORIDADE: (X) Essencial ( ) Importante; ( ) Desejável.
    """
    
    nomeMenu("Menu Inicial")
    
    centralizado("(1)   Cadastrar usuário")
    centralizado("(2)   Cadastrar livro")
    centralizado("(3)   Buscar livro")
    centralizado('(4)   Visualizar empréstimos')
    centralizado("(5)   Remover livro")
    centralizado("(6)   Remover usuário")
    centralizado("(7)   Sair da conta")
    
    # opções que somente o gerente consegue acessar
    if gerente:
        centralizado("(8)   Aprovar Funcionário")
        centralizado("(9)   Remover Funcionário")
    
    centralizado("(0)   Encerrar o programa")

    print("\n" + "="*60 + "\n")
    opcao = input("Selecione uma opção:")
    
    # analisando o input
    if opcao == "1":
        from opcoesUsuario import cadastraUsuario
        print("\nRedirecionando para a tela de cadastro de usuário...\n")
        return cadastraUsuario()
        
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    elif opcao == "6":
        pass
    elif opcao == "7":
        pass
    elif (opcao == "8") and (gerente == True):
        pass
    elif (opcao == "9") and (gerente == True):
        pass
    elif opcao == "0":
        print("\nSaindo do arcevo bibliotecário...\n")
        return False
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuFuncionario()