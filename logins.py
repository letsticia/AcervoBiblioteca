""" Módulo das funções necessárias para o login. """

from formatacao import *
from valida import *

def cadastroFuncionario():
    """Cumpre o requisito [RF002] Cadastro Funcionário(a):\n
    O sistema deve possibilitar que o funcionário(a) realize o cadastro a partir de suas credenciais a seguir: nome completo, e-mail, telefone, cidade/estado, CPF e data de nascimento e uma senha.\n
    PRIORIDADE: ( ) Essencial; (X) Importante; ( ) Desejável.
    """
    
    nomeMenu("Cadastro de Funcionário")
    
    nome = inputCentralizado(f"{'[Nome Completo':<32}]: ")
    
    email = inputCentralizado(f"{'[E-mail':<32}]:")
    
    if not validaEmail(email):
        print("ERRO: e-mail inválido\nPor favor, insira um e-mail válido")
        return cadastroFuncionario()
    
    telefone = inputCentralizado(f"{'[Telefone':<32}]: ")
    cep = inputCentralizado(f"{'[Cidade e Estado':<32}]: ")
    nascimento = inputCentralizado(f"{'[Data de Nascimento (dd/mm/aaaa)':<32}]: ")
    senha = inputCentralizado(f"{'[Senha':<32}]: ")
        
    


def loginGerente():
    """Cumpre o requisito [RF003] Login gerente:\n
    O sistema deve possibilitar que o gerente realize cadastro no sistema com seu CPF e sua senha.\n
    PRIORIDADE: ( ) Essencial; ( ) Importante; (X) Desejável.
    """

    nomeMenu("Login do Gerente")
    
def loginFuncionario():
    """Cumpre o requisito [RF004] Login Funcionário(a):\n
    O sistema deve possibilitar que o funcionário(a) realize login no sistema com suas credenciais de CPF e senha.\n
    PRIORIDADE: ( ) Essencial; (X) Importante; ( ) Desejável.
    """
    nomeMenu("Login do Funcionário")
    