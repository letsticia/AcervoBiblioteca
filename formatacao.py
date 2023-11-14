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
