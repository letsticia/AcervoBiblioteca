from tinydb import TinyDB

db = TinyDB('db.json')
tabelaSolicitacaoFuncionarios = db.table("SolicitacaoFuncionarios")
tabelaFuncionarios = db.table("Funcionários")
