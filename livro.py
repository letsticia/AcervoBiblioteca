"""Arquivo criador do objeto Livro."""

from formatacao import substituiAcento

class Livro:
    def __init__(self, nome, autor, editora, ano, cadastro, status, numID, entrega):
        self.nome = substituiAcento(nome.title())
        self.autor = substituiAcento(autor.title())
        self.editora = substituiAcento(editora.title())
        self.ano = ano
        self.cadastro = cadastro
        self.status = status
        self.numID = numID
        self.entrega = entrega