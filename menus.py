"""Módulo com as funções das telas de menu."""

from formatacao import *
from conector import tabelaFuncionarioOnline, tabelaEmprestimos
from datetime import date 

def menuInicial():
    # removendo o funcionário que estava online
    tabelaFuncionarioOnline.truncate()
    
    # recebendo os dados do dia de hoje
    hoje = date.today()
    dataHoje = hoje.strftime("%d/%m/%Y")
    
    # analisando se algum empréstimo está vencido
    for itens in tabelaEmprestimos:
        if itens['entrega'] < dataHoje:
            itens.update({'status': 'vencido'})
    
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

def menuFuncionario(gerente):
    """Cumpre o requisito [RF008] Menu funcionário:
    Após a entrada do usuário no sistema ele terá um menu com as seguintes opções: cadastrar
    usuário, cadastrar livro, buscar livro, empréstimos, remover livro, remover usuário, logout.
    PRIORIDADE: (X) Essencial ( ) Importante; ( ) Desejável.
    """
    
    nomeMenu("Menu Inicial")
    
    centralizado("(1)   Cadastrar usuário")
    centralizado("(2)   Cadastrar livro")
    centralizado("(3)   Buscar livro")
    centralizado('(4)   Empréstimos')
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
        from opcoesLivro import cadastraLivro
        print("\nRedirecionando para a tela de cadastro de livro...\n")
        return cadastraLivro()
    
    elif opcao == "3":
        from opcoesLivro import menuBuscaLivro
        print("\nRedirecionando para a tela de busca de livros...\n")
        return menuBuscaLivro()
    
    elif opcao == "4":
        from emprestimos import menuEmprestimos
        print("\n Redirecionando para o menu de Emprestimos...")
        return menuEmprestimos()
    
    elif opcao == "5":
        pass
    elif opcao == "6":
        pass
    elif opcao == "7":
        print("\nRedirecionando para o menu inicial ...\n")
        return menuInicial()
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