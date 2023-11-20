""" Arquivo que permite que os arquivos .json sejam conectados ao tinydb"""

from tinydb import TinyDB

# conectando o tinyDB ao banco dos funcionários
db = TinyDB('funcionarios.json')

# definindo a tabela de solicitação de funcionários
tabelaSolicitacaoFuncionarios = db.table("SolicitacaoFuncionarios")

# definindo a tabela de Funcionários
tabelaFuncionarios = db.table("Funcionarios")

# definindo a tabela de funcionário conectado ao programa
tabelaFuncionarioOnline = db.table("Online")

# conectando o tinyDB ao banco de dados do gerente
dbGerente = TinyDB('gerente.json')

# definindo a tabela Gerente
tabelaGerente = dbGerente.table("gerente")

# dicionário com o email e a senha do gerente
infoGerente = tabelaGerente.all()[0]

# conectando o tinydb ao banco de dados dos usuários
dbUsuarios = TinyDB('usuarios.json')

#definindo tabela Usuário
tabelaUsuario = dbUsuarios.table('Usuarios')