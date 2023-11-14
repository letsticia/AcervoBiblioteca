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
    dado = input(f"{' ':>10}{string}")
    
    return dado