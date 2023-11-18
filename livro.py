"""Arquivo criador do objeto Livro."""

from formatacao import substituiAcento

class Livro:
    def __init__(self, numId, nome, autor, editora, ano, cadastro):
        self.numId = numId 
        self.nome = substituiAcento(nome.title())
        self.autor = substituiAcento(autor.title())
        self.editora = substituiAcento(editora.title())
        self.ano = ano
        self.cadastro = cadastro
        
        