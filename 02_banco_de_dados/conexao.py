import sqlite3

conexao = sqlite3.connect('D:/julia/Desktop/bootcamp_dados/02 exercicio_bd/banco')
cursor = conexao.cursor()

# exercício 1
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# exercício 2
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Jessica", 32, "Ciencia da Computacao")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Thor", 18, "Medicina Veterinaria")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Sula", 62, "Analista de Sistemas")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Paula", 41, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Aurora", 18, "Artista")')

# exercício 3
tabela = cursor.execute('SELECT * FROM alunos')
for alunos in tabela:
    print(alunos)

maior_que_20 = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
for alunos in maior_que_20:
    print(alunos)

cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC;')

# exercício 4
cursor.execute('UPDATE alunos SET idade = 61 WHERE id = 3')
cursor.execute('DELETE FROM alunos WHERE id = 3')

# exercício 5
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Lucia", 32, 205.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Pedro", 24, 306.35)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Victor", 27, 45.56)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Leticia", 35, 206.65)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Bianca", 28, 710.25)')

# exercício 6
maior_30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for clientes in maior_30:
    #print(clientes)

saldo_medio = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
print(saldo_medio.fetchone()[0])

maior_saldo = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes);')
print(maior_saldo.fetchone()[0])

maior_1000 = cursor.execute('SELECT COUNT(*) AS maior_1000 FROM clientes WHERE saldo > 1000;')
print(maior_1000.fetchone()[0])

# exercício 7
cursor.execute('UPDATE clientes SET saldo = 406.35 WHERE id = 2;')
cursor.execute('DELETE FROM clientes WHERE id = 4;')

# exercício 8

cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto TEXT,valor REAL,FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Leite", 7.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, "pao", 15.00);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 3, "cafe", 25.00);')

compras = cursor.execute('SELECT c.nome AS nome_cliente, p.produto, p.valor FROM compras p JOIN clientes c ON p.cliente_id = c.id;')
for resultado in compras:
    nome_cliente, produto, valor = resultado
    print(f"Nome do Cliente: {nome_cliente}, Produto: {produto}, Valor: {valor}")

conexao.commit()
conexao.close