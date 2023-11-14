"""Módulo com as funções para a validação do cadastro de funcionários."""


def validaEmail(email):
    """valida se o e-mail digitado é válido

    Args:
        email (str): e-mail a ser validado

    Returns:
        Bool: se válido, True, senão, False
    """
    return (('@' in email) and (('.com' or '.org' or '.br') in email))

def validaSenha(senha):
    """Valida se a senha possui 8 caracteres ou mais

    Args:
        senha (str): senha a ser validada

    Returns:
        Bool: se válido, True, senão, False
    """
    return (len(senha) >= 8)

def validaTelefone(telefone):
    pass