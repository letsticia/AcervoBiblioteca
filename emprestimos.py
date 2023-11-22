from formatacao import *
from menus import *

def menuEmprestimos():
    
    """ Cumpre o requisito [RF012] Empréstimos:\n
    O sistema deve possibilitar que o funcionário(a) entre na aba de empréstimos que contém as
    seguintes opções: Realizar empréstimos, visualizar empréstimos, status do empréstimo,
    renovar empréstimos.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    nomeMenu('Menu de empréstimos')
    
    centralizado("(1)   Realizar empréstimo")
    centralizado("(2)   Visualizar empréstimos")
    centralizado("(3)   Status do empréstimo")
    centralizado("(4)   Renovar empréstimo")
    centralizado("(5)   Voltar ao menu do Funcionário")
    
    print("\n" + "="*60 + "\n")
    opcao = input("Selecione uma opção:")
    
    