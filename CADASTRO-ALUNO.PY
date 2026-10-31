import sqlite3


conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota REAL
    )
''')


nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = float(input("Digite a nota do aluno: "))

cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)", (nome_aluno, nota_aluno))

conexao.commit()
print("Dado salvo no SQL com sucesso!")
conexao.close()
