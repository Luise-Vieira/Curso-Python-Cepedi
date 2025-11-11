# Questão 1 e 2 de matrizes

matriz=[[1, 2],[3, 4]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()


matriz2=[[],[],[]]

for i in range(3):
    for j in range(3):
        num=int(input(f"Digite o valor da {i+1} linha e da {j+1} coluna "))
        matriz2[i].append(num)
    print()

for i in range(3):
    for j in range(3):
        print(matriz2[i][j], end=" ")
    print()



  