from menus import menuFuncionario
from formatacao import *
from valida import validaObrigatoriedade, validaAno
from livro import Livro
from conector import *

def cadastraLivro():
    """Cumpre o requisito [RF010] Cadastrar Livro: \n
    O sistema deve possibilitar que o funcionário(a) realize o cadastro de livros no sistema,
    informando o id , nome, autor, editora, ano.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável."""
    
    nomeMenu("Cadastro de Livro")
    
    nome = inputCentralizado(f"[{'Nome':<29}]: ")
    
    # validando o nome
    if not validaObrigatoriedade(nome):
        return cadastraLivro()
    
    autor = inputCentralizado(f"[{'Autor':<29}]: ")
    
    # validando autor
    if not validaObrigatoriedade(autor):
        return cadastraLivro()
    
    editora = inputCentralizado(f"[{'Editora':<29}]: ")
    
    # validando editora
    if not validaObrigatoriedade(editora):
        return cadastraLivro()
    
    ano = inputCentralizado(f"[{'Ano de Publicacao (4 dígitos)':<29}]: ")
    
    # validando o ano de publicacao
    if not validaAno(ano):
        print("ERRO: Digite um ano válido")
        return cadastraLivro()
    
    infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
    
    # obtendo o nome do funcionário que cadastrou
    cadastro = infoFuncionarioOnline['nome']
    
    numID = tabelaNumID.all()[0]["ID"]
    
    # criando o objeto livro
    novoLivro = Livro(nome, autor, editora, ano, cadastro, "Disponivel", numID)
    
    # colocando o objeto no banco de dados
    tabelaLivros.insert(novoLivro.__dict__)
    
    print("Livro cadastrado com sucesso!")
    
    tabelaNumID.update({'ID': numID+1})
    
    return voltaMenu()
    
def menuBuscaLivro():
    """Cumpre o requisito [RF011] Buscar livro \n
    O sistema deve possibilitar que o funcionário(a) busque o livro ou no caso filtre a busca do
    livro a partir de qualquer uma de suas credenciais.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    nomeMenu("Buscar um livro")
    
    centralizado("(1)   Procurar por nome")
    centralizado("(2)   Procurar por autor")
    centralizado("(3)   Procurar por data de lançamento")
    centralizado("(4)   Procurar por editora")
    centralizado("(5)   Voltar ao menu de Funcionários")
    
    print("\n" + "="*60 + "\n")
    
    opcao = input("Selecione uma opção:")
    
    # busca por nome do livro
    if opcao == "1":
        livroConsulta = Query()
        nome = input("Digite o nome do autor:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.nome == substituiAcento(nome.title())))
        
        if resultado == []:
            print('Não foi encontrado nenhum livro com esse nome')
            return menuBuscaLivro()
        else:
            nomeMenu('Resultado da busca')
            resultadoBusca(resultado[0])
            return voltaMenu()

    # busca por autor(a)    
    elif opcao == "2":
        livroConsulta = Query()
        autor = input("Digite o nome do autor:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.autor == substituiAcento(autor.title())))
        
        if resultado == []:
            print('Não foi encontrado nenhum livro com esse(a) autor(a)')
            return menuBuscaLivro()
        else:
            nomeMenu('Resultado da busca')
            for itens in resultado:
                resultadoBusca(itens)
            return voltaMenu()
        
    # busca por data de lançamento    
    elif opcao == "3":
        livroConsulta = Query()
        data = input("Digite a data de lançamento:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.ano == data))
        
        if resultado == []:
            print('Não foi encontrado nenhum livro com essa data de lancamento')
            return menuBuscaLivro()
        else:
            nomeMenu('Resultado da busca')
            
            for itens in resultado:
                resultadoBusca(itens)
            return voltaMenu()
        
    # busca por editora    
    elif opcao == "4":
        
        livroConsulta = Query()
        editora = input("Digite o nome da editora:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.editora == substituiAcento(editora.title())))
        
        if resultado == []:
            print('Não foi encontrado nenhum livro pulicado por essa editora')
            return menuBuscaLivro()
        else:
            nomeMenu('Resultado da busca')
            for itens in resultado:
                resultadoBusca(itens)
            return voltaMenu()
        
    elif opcao == "5":
        print("Redirecionando para o menu do funcionário...")
        return voltaMenu()
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuBuscaLivro()

def voltaMenu():
    volta = input('\nPressine qualquer tela para voltar ao menu do funcionário')
    infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
    if (infoFuncionarioOnline['nome'] == 'Gerente'):
        return menuFuncionario(True)
    else:
        return menuFuncionario(False)
    
def removerLivro():
    """Cumpre o requisito[RF017] Remover livro:\n
    O sistema deve possibilitar que o funcionário(a) realize a remoção do livro do catálogo,
    informando a justificativa da remoção.\n
    PRIORIDADE: ( ) Essencial; ( ) Importante; (X) Desejável.
    """
    
    nomeMenu('Remover um Livro')
    
    numID = input("Digite o ID do livro a ser removido: ")
        
    # gerará um dicionário
    buscaID = tabelaEmprestimos.search(Query().numID == int(numID))
    
    if buscaID == []:
        print("ID inválido!")
        
        return voltaMenu()
    else:
        
        justificativa = input("Digite a justificativa da remoção: ")
        infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
        
        status = f"Removido por {infoFuncionarioOnline['nome']}. Justificativa: {justificativa}"
        
        tabelaLivros.update({'status': status}, Query().numID == int(numID))
        
        print("O livro foi removido com sucesso e seu status foi atualizado.")
        return voltaMenu()