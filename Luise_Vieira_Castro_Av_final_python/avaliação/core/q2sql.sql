#create database usuario
#use usuario

#create table usuarios
#(
	#id int primary key,
   # nome varchar(50),
   # email varchar(100)
#);

#insert into usuarios(id,nome,email)
#values (1,'Ana','Ana@email.com');

#insert into usuarios(id,nome,email)
#values (2,'João','Joao@gmail.com');

#select * from usuarios;

#create table mensagem
#(
#	identificador int,
#    mensagem varchar(200),
#	foreign key(identificador)
#		references usuarios(id)
#);

#insert into mensagem(identificador,mensagem)
#values (1,'Mensagem para Ana'), (2,'Mensagem para João')

select
	user.nome, men.mensagem from usuarios user
    join mensagem men on user.id = men.identificador;


    
    



    

