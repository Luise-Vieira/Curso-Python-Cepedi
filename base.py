#Base python

#definir variavel
# nome=input("Digite seu nome:")
# print(nome)

# idade=int(input("Digite sua idade"))
# print(f"Meu nome é {nome} e tenho {idade} anos")

#operadores

# + soma
# - sub
# * Mult
#/ div, // div inteira
# % mod
#** potencia

#operador logico
# and or not

# if condiçao : se
#elif condicao : se nao se
#else:

#switch case do python:
# #match op:
#     case 1:
#     case 2:

#estruturas de repetição
#for i in range(5):
    # acao
    # range(5)= 0 a 4

#while condiçao:

#do while(n existe ent é simulado)
# #while True:
#     n = int(input("Digite um número (-1 para sair): "))
#     if n == -1:
#         break

#lista
#começa em zero, tem ordem por indices e é mutavel( igual em C)
#notas=[7,8,4,2]
#print(notas[0]) #7

#append adiciona no final
#notas.append(6)

#insert add em posição especifica
#notas.insert(1,9) #adiciona na posição 1 o numero 9

#remove pelo valor notas.remove(8)
#remove pelo indice notas.pop(0)

#como percorre listas?
#for nota in notas:
    #print(nota)

#for i in range(len(notas)) #len é para tamanho
    #print(notas[i])

#tuplas sao listas imutaveis

#cores=("azul,"verde","vermelho")
#print(cores[1])

#dicionarios
#Chave e valor
#aluno={
# "nome": "Joao",
# "idade": 20,
# "curso": "SI"
# }

#print(aluno["nome"]) ou print(aluno.get("nome"))

#try - except

# try:
#     x = int("abc")
# except Exception as erro:
#     print(erro)

#funções 

# def ola():
#     print("ola")

#ola()

# def ola(nome):
#     print(f"Olá, {nome}")

# ola("ise")

# def adiciona(lista):
#     lista.append(10)

# nums = [1, 2]
# adiciona(nums)
# print(nums)  # [1, 2, 10]

#funções prontas 

# nums = [1, 5, 3]

# sum(nums)  # 9
# max(nums)  # 5
# min(nums)  # 1

#lambda

# nums = [1, 2, 3]

# resultado = list(map(lambda x: x * 2, nums))
# # [2, 4, 6]

#POO(Programação orientada a objetos)
#class é um molde

# class Aluno:
#     def __init__(self, nome, idade, nota): 
#         self.nome = nome
#         self.idade = idade
#         self.nota = nota

#herança

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# class Aluno(Pessoa):
#     def __init__(self, nome, nota):
#         super().__init__(nome) #chama a classe mae
#         self.nota = nota

#polimorfismo

#class Animal:
#     def som(self):
#         pass

# class Cachorro(Animal):
#     def som(self):
#         return "Au"

# class Aluno:
#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota

#     def aprovado(self):
#         return self.nota >= 7

# a1 = Aluno("Lu", 9)
# print(a1.aprovado())

# Classe = molde
# Objeto = coisa criada
# __init__ = inicializa dados
# self = esse objeto
# Método = função do objeto
# POO = organização, não magia

#http
#get -> buscar get/usuarios
#post -> criar
#put -> att
#delete -> apagar

#Django
#model banco de dados
# from django.db import models

# class Aluno(models.Model):
#     nome = models.CharField(max_length=100)
#     idade = models.IntegerField()

# class Curso(models.Model):
#     nome = models.CharField(max_length=100)

# class Aluno(models.Model):
#     nome = models.CharField(max_length=100)
#     # curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

#view logica 
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Olá, mundo")


#template interface

#url
# from django.urls import path
# from .views import home, lista_alunos

# urlpatterns = [
#     path("", home),
#     path("alunos/", lista_alunos),
#]

#banco de dados
-- CRIAR BANCO DE DADOS
# CREATE DATABASE escola;

# -- USAR O BANCO DE DADOS
# USE escola;

# -- CRIAR TABELA COM CHAVE PRIMÁRIA
# CREATE TABLE aluno (
#     id INT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     idade INT
# );

# -- CRIAR OUTRA TABELA COM RELACIONAMENTO
# CREATE TABLE curso (
#     id INT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL
# );

# -- TABELA COM CHAVE ESTRANGEIRA (1:N)
# CREATE TABLE matricula (
#     id INT PRIMARY KEY,
#     aluno_id INT,
#     curso_id INT,
#     FOREIGN KEY (aluno_id) REFERENCES aluno(id),
#     FOREIGN KEY (curso_id) REFERENCES curso(id)
# );

# -- DELETAR UM REGISTRO
# DELETE FROM aluno WHERE id = 1;

# -- DELETAR UMA TABELA
# DROP TABLE aluno;

# -- DELETAR O BANCO DE DADOS
# DROP DATABASE escola;













