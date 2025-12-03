create database alunos;
use alunos;

create table aluno(
id int auto_increment primary key,
nome varchar(50) not null,
telefone varchar(15) not null,
email  varchar(50) not null);