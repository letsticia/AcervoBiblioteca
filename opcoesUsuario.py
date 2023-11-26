"""Módulo em que as opções que envolvem usuários são efetuadas."""

from formatacao import *
from valida import *
from usuario import Usuario
from conector import *
from menus import *

def cadastraUsuario():
    """Cumpre o requisito [RF009] Cadastrar usuário:\n
    O sistema deve possibilitar que o funcionário(a) realize o cadastro de usuários com suas
    credenciais a seguir: nome completo, CPF, telefone, e-mail, idade, instituição, data de
    nascimento, endereço e uma senha.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.

    """
    
    nomeMenu("Cadastro de Usuário")
    
    nome = inputCentralizado(f"{'[Nome Completo':<32}]: ")
    
    if not validaObrigatoriedade(nome):
        return cadastraUsuario()
    
    email = inputCentralizado(f"{'[E-mail':<32}]: ")
    
    # validando o email
    if not validaEmail(email):
        print("\nERRO: e-mail inválido\nPor favor, insira um e-mail válido\n")
        return cadastraUsuario()
    
    idade = inputCentralizado(f"{'[Idade (em números)':<32}]: ")
    
    # validando a idade
    if not validaIdade(idade):
        print("ERRO: digite uma idade válida")
        return cadastraUsuario()
    
    instituicao = inputCentralizado(f"{'[instituicao':<32}]: ")
    
    # validando a instituicao
    if not validaObrigatoriedade(instituicao):
        return cadastraUsuario()
    
    telefone = inputCentralizado(f"{'[DDD + Telefone (apenas números)':<32}]: ")
    
    # validando o telefone
    if not validaTelefone(telefone.replace(" ", "")):
        print("\nERRO: digite um número de telefone válido\n")
        return cadastraUsuario()
        
    cidade = inputCentralizado(f"{'[Cidade':<32}]: ")
    
    # validando a cidade
    if not validaObrigatoriedade(cidade):
        return cadastraUsuario()
    
    estado = inputCentralizado(f"{'[Estado':<32}]: ")
    
    # validando o estado
    if not validaObrigatoriedade(estado):
        return cadastraUsuario()
    
    cpf = inputCentralizado(f"{'[CPF (somente números)':<32}]: ")
    
    # validando o CPF
    if not validaCPF(cpf.replace(" ", "")):
        print("\nERRO: digite um número de CPF válido\n")
        return cadastraUsuario()
    elif ((tabelaUsuario.search(Query().cpf == cpf.replace(" ", ""))) != []):
        print("\nERRO: cpf já cadastrado")
        return cadastraUsuario()
    
    nascimento = inputCentralizado(f"{'[Data de Nascimento (dd/mm/aaaa)':<32}]: ")
    
    # validando data de nascimento
    if not validaNascimento(nascimento):
        print("\nERRO: insira uma data de nascimento válida\n")
        return cadastraUsuario()
    
    senha = inputCentralizado(f"{'[Senha (mínimo de 8 dígitos)':<32}]: ")
    
    # validando a senha
    if not validaSenha(senha):
        print("\nERRO: digite uma senha válida (mínimo de 8 dígitos)\n")
        return cadastraUsuario()
    
    # criando um objeto funcionário
    novoUsuario = Usuario(nome, email, idade, instituicao, telefone, cidade, estado, cpf, nascimento, senha)
    
     # adicionando o funcionário ao banco de dados
    tabelaUsuario.insert(novoUsuario.__dict__)
    
    print("\nUsuário adicionado com sucesso! Voltando ao menu principal...\n")
    volta = input('\nUsuário adicionado com sucesso!\nPressine qualquer tela para voltar ao menu do funcionário')
    infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
    if (infoFuncionarioOnline['nome'] == 'Gerente'):
        return menuFuncionario(True)
    else:
        return menuFuncionario(False)

def removerUsuario():
    """Cumpre o requisito [RF018] Remover usuário:\n
    O sistema deve possibilitar que o funcionário(a) remova o usuário do sistema caso o usuário
    queira remover seus dados do sistema.\n
    PRIORIDADE: (X) Essencial; ( ) Importante; ( ) Desejável.
    """
    
    nomeMenu("Remover usuário")
    
    cpf = input("Digite o cpf do usuário a ser removido: ")
    
     # retorna um único dicionário dentro de uma lista
    buscaUsuario = (tabelaUsuario.search(Query().cpf == cpf))
    
    if buscaUsuario == []:
        volta = input('\nERRO: usuário não encontrado!\nPressine qualquer tela para voltar ao menu do funcionário')
        infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
        if (infoFuncionarioOnline['nome'] == 'Gerente'):
            return menuFuncionario(True)
        else:
            return menuFuncionario(False)
    else:
        tabelaUsuario.remove(Query().cpf == cpf)
        volta = input('\nUsuário removido!\nPressine qualquer tela para voltar ao menu do funcionário')
        infoFuncionarioOnline = tabelaFuncionarioOnline.all()[0]
        if (infoFuncionarioOnline['nome'] == 'Gerente'):
            return menuFuncionario(True)
        else:
            return menuFuncionario(False)