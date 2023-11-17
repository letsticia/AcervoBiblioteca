""" Módulo das funções necessárias para o login. """

from formatacao import *
from valida import *
from funcionario import Funcionario
from conector import *
from menus import menuInicial

def cadastroFuncionario():
    """Cumpre o requisito [RF002] Cadastro Funcionário(a):\n
    O sistema deve possibilitar que o funcionário(a) realize o cadastro a partir de suas credenciais a seguir: nome completo, e-mail, telefone, cidade/estado, CPF e data de nascimento e uma senha.\n
    PRIORIDADE: ( ) Essencial; (X) Importante; ( ) Desejável.
    """
    
    nomeMenu("Cadastro de Funcionário")
    
    nome = inputCentralizado(f"{'[Nome Completo':<32}]: ")
    
    if not validaObrigatoriedade(nome):
        return cadastroFuncionario()
    
    email = inputCentralizado(f"{'[E-mail':<32}]: ")
    
    # validando o email
    if not validaEmail(email):
        print("\nERRO: e-mail inválido\nPor favor, insira um e-mail válido\n")
        return cadastroFuncionario()
    
    telefone = inputCentralizado(f"{'[DDD + Telefone (apenas números)':<32}]: ")
    
    # validando o telefone
    if not validaTelefone(telefone.replace(" ", "")):
        print("\nERRO: digite um número de telefone válido\n")
        return cadastroFuncionario()
        
    cidade = inputCentralizado(f"{'[Cidade':<32}]: ")
    
    # validando a cidade
    if not validaObrigatoriedade(cidade):
        return cadastroFuncionario()
    
    estado = inputCentralizado(f"{'[Estado':<32}]: ")
    
    # validando o estado
    if not validaObrigatoriedade(estado):
        return cadastroFuncionario()
    
    cpf = inputCentralizado(f"{'[CPF (somente números)':<32}]: ")
    
    # validando o CPF
    if not validaCPF(cpf.replace(" ", "")):
        print("\nERRO: digite um número de CPF válido\n")
        return cadastroFuncionario()
    
    nascimento = inputCentralizado(f"{'[Data de Nascimento (dd/mm/aaaa)':<32}]: ")
    
    # validando data de nascimento
    if not validaNascimento(nascimento):
        print("\nERRO: insira uma data de nascimento válida\n")
        return cadastroFuncionario()
    
    senha = inputCentralizado(f"{'[Senha (mínimo de 8 dígitos)':<32}]: ")
    
    # validando a senha
    if not validaSenha(senha):
        print("\nERRO: digite uma senha válida (mínimo de 8 dígitos)\n")
        return cadastroFuncionario()
    
    # criando um objeto funcionário
    novoFuncionario = Funcionario(nome, email, telefone, cidade, estado, cpf, nascimento, senha)
    
    # adicionando o funcionário ao banco de dados
    tabelaSolicitacaoFuncionarios.insert(novoFuncionario.__dict__)
    
    print("\nFuncionário adicionado com sucesso! Voltando ao menu Inicial...\n")
    return menuInicial()

def loginGerente():
    """Cumpre o requisito [RF003] Login gerente:\n
    O sistema deve possibilitar que o gerente realize cadastro no sistema com seu CPF e sua senha.\n
    PRIORIDADE: ( ) Essencial; ( ) Importante; (X) Desejável.
    """

    nomeMenu("Login do Gerente")
    
    cpf = inputCentralizado(f"{'[CPF':<5}]: ")
    senha = inputCentralizado(f"{'[Senha':<5}]: ")
    
    # comparando as informações do gerente com as informações digitadas
    if (cpf == infoGerente['cpf']) and (senha == infoGerente['senha']):
        pass
    else:
        print("ERRO: Informações inválidas, redirencionando para o menu\ninicial...")
        return menuInicial()
    
def loginFuncionario():
    """Cumpre o requisito [RF004] Login Funcionário(a):\n
    O sistema deve possibilitar que o funcionário(a) realize login no sistema com suas credenciais de CPF e senha.\n
    PRIORIDADE: ( ) Essencial; (X) Importante; ( ) Desejável.
    """
    nomeMenu("Login do Funcionário")
    