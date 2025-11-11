matriz1=[]
matriz2=[]
resultado=[]

print("Maytriz 1")
for i in range(2):
    linha=[]
    for j in range(2):
        valor=int(input(f"[{i+1}], [{j+1}]"))
        linha.append(valor)
    matriz1.append(linha)

print("Matriz 2")

for i in range(2):
    linha=[]
    for j in range(2):
        valor=int(input(f"[{i+1}], [{j+1}]"))
        linha.append(valor)
    matriz2.append(linha)

print("Soma das matrizes")

for i in range(2):
    linha=[]
    for j in range(2):
        soma=matriz1[i][j] + matriz2[i][j]
        linha.append(soma)
    resultado.append(linha)

print("Resultado")
for linha in resultado:
    print(linha)








