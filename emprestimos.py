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
    centralizado("(2)   Historico de empréstimos")
    centralizado("(3)   Status dos empréstimos")
    centralizado("(4)   Renovar empréstimo")
    centralizado("(5)   Voltar ao menu do Funcionário")
    
    print("\n" + "="*60 + "\n")
    opcao = input("Selecione uma opção:")
    
    # analisando o input
    if opcao == "1":        
        return realizaEmprestimo()

    elif opcao == "2":
        return historicoEmprestimo()
    
    elif opcao == "3":
        return statusEmprestimo()
    
    elif opcao == "4":
        return renovaEmprestimo()
    
    elif opcao == "5":
        volta = input('\nPressine qualquer tela para voltar ao menu do funcionário')
        infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
        if (infoFuncionarioOnline['nome'] == 'Gerente'):
            return menuFuncionario(True)
        else:
            return menuFuncionario(False)
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuInicial()
    
def realizaEmprestimo():
    """Cumpre o requisito [RF013] Realizar empréstimos:\n
    O sistema deve possibilitar que o funcionário(a) realize um empréstimo de algum livro no
    nome de um usuário, que deverão ser confirmados com o CPF e senha do usuário\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    nomeMenu("Realizar Empréstimo")
    
    numID = inputCentralizado(f"[{'Id do livro':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaLivro = (tabelaLivros.search(Query().numID == int(numID)))
    
    if buscaLivro == []:
        print("\nERRO: ID inválido, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    elif buscaLivro[0]['status'] != 'Disponivel':
        print("\nERRO: esse livro já fora emprestado")
        return menuEmprestimos()
    
    cpf = inputCentralizado(f"[{'CPF do usuário':<16}]: ")
    senha = inputCentralizado(f"[{'Senha do usuário':<16}]: ")
    
    # retorna um único dicionário dentro de uma lista
    buscaUsuario = (tabelaUsuario.search(Query().cpf == cpf))
    
    if buscaUsuario == []:
        print("\n ERRO: usuário não encontrado, voltando ao menu de empréstimos...")
        return menuEmprestimos()
    
    elif (buscaUsuario[0]['cpf'] == cpf) and (buscaUsuario[0]['senha'] == senha):
        
        # obtendo a data do dia da realização do emprestimo
        hoje = date.today()
        entrega = (hoje + timedelta(days=15))
        dataentrega = entrega.strftime("%d/%m/%Y")
        dataHoje = hoje.strftime("%d/%m/%Y")
        
        # atualizando os status do livro
        buscaLivro[0].update({'status': 'Emprestado'})

        tabelaEmprestimos.insert({'nome': buscaUsuario[0]['nome'],
                                  'cpf': buscaUsuario,
                                  'livro': buscaLivro[0]['nome'],
                                  'numID': buscaLivro[0]['numID'],
                                  'realizado':dataHoje,
                                  'entrega': dataentrega,
                                  'status': 'ativo'})
        
        print("\n Empréstimo realizado com sucesso!")
        return menuEmprestimos()
    
    else:
        print("\n ERRO: senha incorreta, voltando ao menu de empréstimos...")
        return menuEmprestimos()

def historicoEmprestimo():
    nomeMenu("Histórico de Empréstimos")
    
    # os itens dentro da tabela de empréstimos são dicionários, o resultado da busca ira mostrá os itens dos dicionários
    for itens in (tabelaEmprestimos.all()):
        resultadoBusca(itens)
    
    volta = input('\nPressine qualquer tela para voltar ao menu de empréstimos')
    return menuEmprestimos()

def statusEmprestimo():
    """Cumpre o requisito [RF015] Status empréstimo:\n
    O sistema deve possibilitar que o funcionário(a) visualize o status do empréstimo para saber
    se ele está ativo ou vencido, nisso ele terá também a opção de confirmar a devolução.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    
    nomeMenu('Status dos Emprestimos')
    
    # Ambod retornam uma lista que contém os dicionários correspondente aos empréstimos
    buscaEmprestimo = tabelaEmprestimos.search(Query().status == 'ativo')
    buscaVencido = tabelaEmprestimos.search(Query().status == 'vencido')
    
    if buscaEmprestimo == [] and buscaVencido == []:
        print('Não há empréstimos ativos ou vencidos')
        
        volta = input('\nPressine qualquer tela para voltar ao menu de empréstimos')
        return menuEmprestimos()
    
    if buscaEmprestimo != []:
        nomeMenu('Empréstimos ativos')
        
        for itens in buscaEmprestimo:
            resultadoBusca(itens)
    
    if buscaVencido != []:
        nomeMenu('Empréstimos vencidos')
        
        for itens in buscaVencido:
            resultadoBusca(itens)
    
    print("\n" + "="*60 + "\n")
    
    opcao = input("Deseja confirmar alguma devolução? [S/N]")
    
    if (opcao.title()) == 'S':
        numID = input("Digite o ID do livro a ser devolvido:")
        
        # gerará um dicionário
        buscaID = tabelaEmprestimos.search(Query().numID == numID)
        
        if buscaID == []:
            print("ID inválido ou não pertence a um empréstimo")
            
            volta = input('\nPressine qualquer tela para voltar ao menu de empréstimos')
            return menuEmprestimos()
            
        else:
            hoje = date.today()
            dataHoje = hoje.strftime("%d/%m/%Y")
            
            # gerará um dicionário
            buscaLivro = tabelaLivros.search(Query().numID == numID)[0]
            
            buscaID[0].update({'status': 'devolvido'})
            buscaID[0].update({'entrega': dataHoje })
            buscaLivro.update({'status: Disponível'})
            
            volta = input('\nDevolução confirmada com sucesso!\nPressione qualquer tecla para retornar ao menu de empréstimos.')
            return menuEmprestimos()
    else:
        return menuEmprestimos()
    
def renovaEmprestimo():
    """Cumpre o requisito [RF016] Renovar empréstimo:\n
    O sistema deve possibilitar que o funcionário(a) realize a renovação do empréstimo.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.  
    """
    
    numID = input("Digite o ID do livro a ser renovado:")
        
    # gerará um dicionário
    buscaID = tabelaEmprestimos.search(Query().numID == numID)

    if buscaID == []:
        print("ID inválido ou não pertence a um empréstimo")
        
        volta = input('\nPressine qualquer tela para voltar ao menu de empréstimos')
        return menuEmprestimos()
        
    else:
        hoje = date.today()
        dataHoje = hoje.strftime("%d/%m/%Y")
        
        entrega = (hoje + timedelta(days=15))
        dataentrega = entrega.strftime("%d/%m/%Y")
        
        buscaID[0].update({'realizado': dataHoje})
        buscaID[0].update({'entrega':  dataentrega })
        
        volta = input('\nRenovação concluida com sucesso!\nForam adicionados 15 dias.\nPressione qualquer tecla para retornar ao menu de empréstimos.')
        return menuEmprestimos()