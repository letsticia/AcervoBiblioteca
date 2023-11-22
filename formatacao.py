"""Módulo de formatação das strings. """

def nomeMenu(menu):
    """Cria um cabeçalho.

    Args:
        menu (str): nome do menu
    """
    print("="*60)
    print(f"{menu:^60}")
    print("="*60 + "\n")

def centralizado(string):
    """Formata o print
 
    Args:
        string (str): string a ser centralizada
    """
    print(f"{' ':>15}{string}")

def inputCentralizado(string):
    """Formata o input

    Args:
        string (str): string que ficará dentro do input

    Returns:
        str : resultado do input
    """
    dado = input(f"{string}")
    
    return dado

def substituiAcento(string):
    """Substitui acentos por caracteres sem acentos

    Args:
        string (str): string a ser formatada

    Returns:
        str: string com os acentos substituidos
    """
    from unicodedata import normalize

    result = normalize('NFKD', string).encode('ASCII','ignore').decode('ASCII')
    
    return result

def resultadoBusca(resultado):
    """Mostra o resultado da busca, feito para o menu de livros.

    Args:
        resultado (dict): objeto a ser mostrado"""
    
    nomeMenu('Resultado da busca')
    
    for item in resultado:
        centralizado(f"[{item:<17}]: {resultado[item]}")
        
    print("\n" + "="*60 + "\n")