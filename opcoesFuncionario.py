from formatacao import *
from conector import *
from menus import menuFuncionario

def aprovaFuncionarios():
    """Cumpre o requisito [RF005] Aprovação gerente:
    O sistema deve possibilitar que o gerente após efetuar o login tenha um campo com as
    solicitações de cadastro do funcionário e possa aprová-lo.
    PRIORIDADE: ( ) Essencial; ( ) Importante; (X) Desejável.
    """
    
    numid = 0
    solicitacoes = tabelaSolicitacaoFuncionarios.all()
    
    nomeMenu("Aprovar Funcionário")
    
    for itens in solicitacoes:
        for item in itens:
            centralizado(f"[{item:<17}]: {itens[item]}")
        centralizado(f"[{'ID':<17}]: {solicitacoes[numid].doc_id}")
        print("\n" + "="*60 + "\n")
        numid += 1
    
    opcao = input("Digite o ID do(a) funcionário(a) que desejas aprovar:")
    
    if (tabelaSolicitacaoFuncionarios.contains(doc_id=opcao)):
        tabelaFuncionarios.insert(tabelaSolicitacaoFuncionarios.get(doc_id=opcao))
        volta = input('\nFuncionário aprovado com sucesso! Pressione qualquer tecla para voltar ao menu do Funcionário')
        return menuFuncionario(True)
    else:
        volta = input('\nERRO: Solicitação não encontrada! Pressione qualquer tecla para voltar ao menu do Funcionário')
        return menuFuncionario(True)

def removerFuncionario():
    """Cumpre o requisito [RF006] Exclusão do funcionário:\n
    O sistema deve possibilitar que o gerente possa excluir um funcionário do sistema\n
    PRIORIDADE: ( ) Essencial; (X) Importante; ( ) Desejável
    """
    
    numid = 0
    
    funcionarios = tabelaFuncionarios.all()
    
    nomeMenu("Remover Funcionário")
    
    for itens in funcionarios:
        for item in itens:
            centralizado(f"[{item:<17}]: {itens[item]}")
        centralizado(f"[{'ID':<17}]: {funcionarios[numid].doc_id}")
        print("\n" + "="*60 + "\n")
        numid += 1
    
    opcao = input("Digite o ID do(a) funcionário(a) que desejas remover:")
    
    if (tabelaFuncionarios.contains(doc_id=opcao)):
        tabelaFuncionarios.remove(tabelaFuncionarios.get(doc_id=opcao))
        volta = input('\nFuncionário removido com sucesso! Pressione qualquer tecla para voltar ao menu do Funcionário')
        return menuFuncionario(True)
    else:
        volta = input('\nERRO: Funcionário não encontrado! Pressione qualquer tecla para voltar ao menu do Funcionário')
        return menuFuncionario(True)