from tinydb import TinyDB

# conectando o tinyDB ao banco de dados geral
db = TinyDB('db.json')

# definindo a tabela de solicitação de funcionários
tabelaSolicitacaoFuncionarios = db.table("SolicitacaoFuncionarios")

# definindo a tabela de Funcionários
tabelaFuncionarios = db.table("Funcionários")

# conectando o tinyDB ao banco de dados do gerente
dbGerente = TinyDB('gerente.json')

# definindo a tabela Gerente
tabelaGerente = dbGerente.table("gerente")

# dicionário com o email e a senha do gerente
infoGerente = tabelaGerente.all()[0]