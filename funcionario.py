from formatacao import substituiAcento

class Funcionario:
    def __init__(self, nome, email, telefone, cidade, estado, cpf, nascimento, senha):
        self.nome = substituiAcento(nome.title())
        self.email = email
        self.telefone = int(telefone)
        self.cidade = substituiAcento(cidade.title())
        self.estado = substituiAcento(estado.title())
        self.cpf = cpf
        self.nascimento = nascimento
        self.senha = substituiAcento(senha)
    