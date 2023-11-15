"""Módulo com as funções para a validação do cadastro de funcionários."""

def validaEmail(email):
    """valida se o e-mail digitado é válido

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
    ano = int(data[::-4])
    return (ano >= 2005)