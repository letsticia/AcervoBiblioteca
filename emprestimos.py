from formatacao import *
from menus import *
from conector import *

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
    
def realizaEmprestimo():
    
    numID = inputCentralizado(f"[{'Id do livro':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaLivro = tabelaLivros.search(Query().numID == numID)
    
    if buscaLivro == []:
        print("\n ERRO: ID inválido, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    
    cpf = inputCentralizado(f"[{'CPF do usuário':<16}]: ")
    senha = inputCentralizado(f"[{'Senha do usuário':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaUsuario = tabelaUsuario.search(Query().cpf == cpf)
    
    if buscaUsuario == []:
        print("\n ERRO: usuário não encontrado, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    elif (buscaUsuario[0]['cpf'] == cpf) and (buscaUsuario[0]['senha'] == senha):
        buscaLivro[0].update({'status': 'Emprestado'})
        print("\n Empréstimo realizado com sucesso!")
        return menuEmprestimos()