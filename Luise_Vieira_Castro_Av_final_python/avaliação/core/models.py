from django.db import models

# Create your models here.

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

class mensagem(models.Model):
    texto= models.CharField(max_length=200)
    mensagem_user=models.ForeignKey(usuario, on_delete=models.SET_NULL,null=True)


    
#O django usa o migration para ve quais nao foram aplicadas ainda, em seguida cria as tabelas e colunas e o necessario para relacionar tabelas e salva.