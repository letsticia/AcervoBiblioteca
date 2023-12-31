""" Arquivo que permite que os arquivos .json sejam conectados ao tinydb"""

from tinydb import TinyDB, Query

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

# definindo tabela Usuário
tabelaUsuario = dbUsuarios.table('Usuarios')

# conectando o tinydb ao banco de dados dos livros
dbLivros = TinyDB('livros.json')

# definindo uma tabela para os livros
tabelaLivros = dbLivros.table('Livros')

# conectando o tinydb ao banco de dados de ID's
dbNumID = TinyDB("numID.json")

# criando uma tabela para ID's de livros
tabelaNumID = dbNumID.table("numID")

# conectando o tinydb ao banco de dados dos emprestimos
dbEmprestimos = TinyDB('emprestimos.json')

# criando uma tabela para os empréstimos
tabelaEmprestimos = dbEmprestimos.table('emprestimos')