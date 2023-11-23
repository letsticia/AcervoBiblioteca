from formatacao import *
from menus import *
from conector import *
from datetime import *

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
    """Cumpre o requisito [RF013] Realizar empréstimos:\n
    O sistema deve possibilitar que o funcionário(a) realize um empréstimo de algum livro no
    nome de um usuário, que deverão ser confirmados com o CPF e senha do usuário\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    nomeMenu("Realizar Empréstimo")
    
    numID = inputCentralizado(f"[{'Id do livro':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaLivro = (tabelaLivros.search(Query().numID == numID))[0]
    
    if buscaLivro == []:
        print("\nERRO: ID inválido, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    elif buscaLivro['status'] != 'Disponivel':
        print("\nERRO: esse livro já fora emprestado")
    
    cpf = inputCentralizado(f"[{'CPF do usuário':<16}]: ")
    senha = inputCentralizado(f"[{'Senha do usuário':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaUsuario = (tabelaUsuario.search(Query().cpf == cpf))[0]
    
    if buscaUsuario == []:
        print("\n ERRO: usuário não encontrado, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    
    elif (buscaUsuario['cpf'] == cpf) and (buscaUsuario['senha'] == senha):
        
        # obtendo a data do dia da realização do emprestimo
        hoje = date.today()
        entrega = (hoje + timedelta(days=15))
        dataentrega = entrega.strftime("%d/%m/%Y")
        dataHoje = dataHoje.strftime("%d/%m/%Y")
        
        # atualizando os status do livro
        buscaLivro.update({'status': 'Emprestado'})

        tabelaEmprestimos.insert({'nome': buscaUsuario['nome'],
                                  'cpf': buscaUsuario,
                                  'livro': buscaLivro['nome'],
                                  'realizado':dataHoje,
                                  'entrega': dataentrega})
        
        print("\n Empréstimo realizado com sucesso!")
        return menuEmprestimos()
    
    else:
        print("\n ERRO: senha incorreta, voltando ao menu de empréstimos...")
        return menuEmprestimos()

def visualizaEmprestimo():
    nomeMenu("Visualizar Empréstimos")
    
    buscaEmprestimo = tabelaLivros.search(Query().status == "Emprestado")
    