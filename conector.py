from tinydb import TinyDB

db = TinyDB('db.json')
tabelaFuncionarios = db.table("Funcionários")
tableaGerente = db.table("Gerente")
