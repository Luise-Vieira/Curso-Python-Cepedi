#Pedro Henrique Santos
#Luise Vieira Castro

import os
import mysql.connector


def conectar_db():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            db='alunos',
            user='root',
            password='root',
        )
        print("Conexão bem-sucedida ao banco de dados.")
        return conexao
    except Exception as erro:
        print("Erro ao conectar ao banco de dados:", erro)
        return None


def cadastro(nome, telefone, email):
    conexao = conectar_db()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO aluno (nome, telefone, email) VALUES (%s, %s, %s)"
        valores = (nome, telefone, email)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Aluno cadastrado com sucesso!\n")
    except Exception as erro:
        print("Erro ao cadastrar aluno:", erro)
    finally:
        cursor.close()
        conexao.close()


def listar():
    conexao = conectar_db()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        sql = "SELECT id, nome, telefone, email FROM aluno"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum aluno cadastrado.\n")
            return

        print("Lista de alunos cadastrados:")
        for row in resultados:
            print(
                f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}, Email: {row[3]}")
        print()
    except Exception as erro:
        print("Erro ao listar alunos:", erro)
    finally:
        cursor.close()
        conexao.close()


def localizar(id):
    conexao = conectar_db()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        sql = "SELECT id, nome, telefone, email FROM aluno WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado is None:
            print("Aluno não encontrado.\n")
            return

        print(
            f"ID: {resultado[0]}, Nome: {resultado[1]}, Telefone: {resultado[2]}, Email: {resultado[3]}\n")
    except Exception as erro:
        print("Erro ao localizar aluno:", erro)
    finally:
        cursor.close()
        conexao.close()


def atualizar_telefone(id, telefone):
    conexao = conectar_db()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        sql = "UPDATE aluno SET telefone = %s WHERE id = %s"
        valores = (telefone, id)
        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.\n")
            return

        print("Telefone atualizado com sucesso!\n")
    except Exception as erro:
        print("Erro ao atualizar telefone:", erro)
    finally:
        cursor.close()
        conexao.close()


def excluir(id):
    conexao = conectar_db()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM aluno WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.\n")
            return

        print("Aluno excluído com sucesso!\n")
    except Exception as erro:
        print("Erro ao excluir aluno:", erro)
    finally:
        cursor.close()
        conexao.close()


opc = -1
while opc != 0:
    print("Sistema de cadastro de alunos")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Localizar um aluno por ID")
    print("4 - Atualizar telefone de um aluno")
    print("5 - Excluir um aluno")
    print("0 - Sair")

    opc = int(input("Escolha uma opção: "))

    match opc:
        case 1:
            print("Cadastrar aluno")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cadastro(nome, telefone, email)
        case 2:
            listar()
        case 3:
            print("Localizar um aluno por ID")
            id = input("ID do aluno: ")
            localizar(id)
        case 4:
            print("Atualizar telefone de um aluno")
            id = input("ID do aluno: ")
            telefone = input("Novo telefone: ")
            atualizar_telefone(id, telefone)
        case 5:
            print("Excluir um aluno")
            id = input("ID do aluno: ")
            excluir(id)
        case 0:
            print("Saindo do sistema.")
        case _:
            print("Opção inválida!")
