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
    
    nome = inputCentralizado(f"[{'Nome':<29}]")
    
    # validando o nome
    if not validaObrigatoriedade(nome):
        return cadastraLivro()
    
    autor = inputCentralizado(f"[{'Autor':<29}]")
    
    # validando autor
    if not validaObrigatoriedade(autor):
        return cadastraLivro()
    
    editora = inputCentralizado(f"[{'Editora':<29}]")
    
    # validando editora
    if not validaObrigatoriedade(editora):
        return cadastraLivro()
    
    ano = inputCentralizado(f"[{'Ano de Publicacao (4 dígitos)':<29}]")
    
    # validando o ano de publicacao
    if not validaAno(ano):
        print("ERRO: Digite um ano válido")
        return cadastraLivro()
    
    infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
    
    # obtendo o nome do funcionário que cadastrou
    cadastro = infoFuncionarioOnline['nome']
    
    # criando o objeto livro
    novoLivro = Livro(nome, autor, editora, ano, cadastro, "Disponivel")
    
    # colocando o objeto no banco de dados
    tabelaLivros.insert(novoLivro.__dict__)
    
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
    
    if opcao == "1":
        livroConsulta = Query()
        nome = input("Digite o nome do autor:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.nome == substituiAcento(nome.title())))[0]
        
        if resultado == []:
            print('Não foi encontrado nenhum livro com esse nome')
            return menuBuscaLivro()
        else:
            resultadoBusca(resultado)
            
            volta = input('Pressine qualquer tela para voltar ao menu de busca')
            return menuBuscaLivro()

        
    elif opcao == "2":
        
        livroConsulta = Query()
        autor = input("Digite o nome do autor:")
        
        # definindo o resultado da busca
        resultado = (tabelaLivros.search(livroConsulta.autor == substituiAcento(autor.title())))
        
        if resultado == []:
            print('Não foi encontrado nenhum livro com esse(a) autor(a)')
        else:
            for itens in resultado:
                resultadoBusca(itens)
                
            volta = input('Pressine qualquer tela para voltar ao menu de busca')
            return menuBuscaLivro()
        
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    else:
        print("\nPor favor selecione uma opção válida\n")
        return menuBuscaLivro()

def realizaEmprestimo(livro):
    pass