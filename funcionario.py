class Funcionario:
    def __init__(self, nome, email, telefone, cidade, estado, cpf, nascimento, senha):
        self.nome = nome.title()
        self.email = email
        self.telefone = int(telefone)
        self.cidade = cidade
        self.estado = estado
        self.cpf = cpf
        self.nascimento = nascimento
        self.senha = senha
    