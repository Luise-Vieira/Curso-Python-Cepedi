matriz=[]
print("Digite os nomes da matriz 2x3")
for i in range(2):
    linha=[]
    for j in range(3):
        nome=input(f"{i+1} {j+1}")
        linha.append(nome)
    matriz.append(linha)

for linha in matriz:
    print(linha)