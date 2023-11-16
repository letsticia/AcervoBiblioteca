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
        loginGerente()
    elif opcao == "2":
        print("\nRedirecionando para a tela de Login de Funcionário...\n")
        from logins import loginFuncionario
        loginFuncionario()
    elif opcao == "3":
        print("\nRedirecionando para a tela de Cadastro de Funcionário...\n")
        from logins import cadastroFuncionario
        cadastroFuncionario()
    elif opcao == "4":
        print("\nSaindo do arcevo bibliotecário...\n")
        return False
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuInicial()
