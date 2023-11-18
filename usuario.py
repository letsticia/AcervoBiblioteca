"""Arquivo criador do objeto Usuário."""

from formatacao import substituiAcento

class Usuario:
    def __init__(self, nome, email, idade, instituicao, telefone, cidade, estado, cpf, nascimento, senha):
        self.nome = substituiAcento(nome.title())
        self.email = email
        self.idade = int(idade)
        self.instituicao = substituiAcento(instituicao.title())
        self.telefone = int(telefone)
        self.cidade = substituiAcento(cidade.title())
        self.estado = substituiAcento(estado.title())
        self.cpf = cpf
        self.nascimento = nascimento
        self.senha = substituiAcento(senha)