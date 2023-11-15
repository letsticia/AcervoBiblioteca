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
        print("Redirecionando para a tela de Login de Gerente...")
        from logins import loginGerente
        loginGerente()
    elif opcao == "2":
        print("Redirecionando para a tela de Login de Funcionário...")
        from logins import loginFuncionario
        loginFuncionario()
    elif opcao == "3":
        print("Redirecionando para a tela de Cadastro de Funcionário...")
        from logins import cadastroFuncionario
        cadastroFuncionario()
    elif opcao == "4":
        print("Saindo do arcevo bibliotecário...")
        return False
    else:
        print("Por favor selecione uma opção válida")
        return menuInicial()
