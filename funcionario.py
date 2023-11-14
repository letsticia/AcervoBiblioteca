class Funcionario:
    def __init__(self, nome, email, telefone, cep, cpf, nascimento, senha):
        self.nome = nome.title()
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.cpf = cpf
        self.nascimento = nascimento
        self.senha = senha
    