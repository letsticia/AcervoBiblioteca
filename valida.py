"""Módulo com as funções para a validação do cadastro de funcionários."""

def validaObrigatoriedade(campo):
    """Valida se foi digitado alguma coisa em um campo obrigatório.

    Args:
        campo (str): campo a ser analisado

    Returns:
        Bool: se válido, True, senão, False
    """
    if campo == "":
        print("ERRO: Esse campo é obrigatório! Por favor, insira a informação necessária")
        return False
    else:
        return True
    
def validaEmail(email):
    """Valida se o e-mail digitado é válido

    Args:
        email (str): e-mail a ser validado

    Returns:
        Bool: se válido, True, senão, False
    """
    return (('@' in email) and (('.com' or '.org' or '.br') in email))

def validaCPF(cpf):
    """Valida o número do cpf

    Args:
        cpf (str): cpf digitado pelo usuário

    Returns:
        Bool: se válido, True, senão, False
    """
    return ((len(cpf) == 11) and (cpf.isnumeric())) 

def validaSenha(senha):
    """Valida se a senha possui 8 caracteres ou mais

    Args:
        senha (str): senha a ser validada

    Returns:
        Bool: se válido, True, senão, False
    """
    return (len(senha) >= 8)

def validaTelefone(telefone):
    """Valida o número de telefone.

    Args:
        telefone (str): conteúdo do input do usuário no campo telefone.
    
    Returns:
        Bool: se válido, True, senão, False
    """
    
    return ((len(telefone) == 11) and (telefone.isnumeric())) 

def validaNascimento(data):
    """Valida a data de nascimento

    Args:
        data (str): data de nascimento inserida pelo usuário

    Returns:
        Bool: se válido, True, senão, False
    """
    ano = int(data[-4::])
    return ((ano >= 2005) and (len(data) >= 8))

def validaIdade(idade):
    """Valida a idade digitada.

    Args:
        idade (str): conteúdo do input do usuário no campo idade.
    
    Returns:
        Bool: se válido, True, senão, False
    """
    
    return (idade.isnumeric())

def validaAno(ano):
    """ Valida se, no campo de ano, fora digitado um número de 4 dígitos

    Args:
        ano (str): _description_

    Returns:
        Bool: se válido, True, senão, False
    """
    
    return (len(ano) == 4) and (ano.isnumeric())