class usuario:
    def __init__(self,id,nome,email):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
         return{
            "id": self.id,
            "Nome": self.nome,
            "email": self.email
        }
    

user1 = usuario(1,"João","joao@gmail.com")
user2 = usuario(2,"Maria","maria@gmail.com")

print(user1.to_dict())
print(user2.to_dict())



