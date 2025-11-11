#3 & 4 & 5
matriz1=[]
soma_coluna=[0,0,0]

print("Matriz 1 e soma das linhas")
for i in range(3):
    linha=[]
    soma_linha=0
    
    for j in range(3):
        valor=int(input(f"[{i+1}], [{j+1}]"))
        linha.append(valor)
        soma_linha+=valor
        soma_coluna[j]+=valor
    matriz1.append(linha)
    print(f"Soma da linha {i+1}: {soma_linha}")
print(f"Soma da coluna {j+1}: {soma_coluna}")

soma_diagonalprin=0
soma_diagonalsecund=0
for i in range(3):
    for j in range(3):
        if i==j:
            soma_diagonalprin+=matriz1[i][j]
            
        if  i + j == len(matriz1)-1:
            soma_diagonalsecund+=matriz1[i][j]
            
        

for linha in matriz1:
    print(linha)

print("\n Somas Finais das Colunas")
print(soma_coluna)

print("\n Soma das diagonais")
print(soma_diagonalprin)
print(soma_diagonalsecund) 

if soma_diagonalprin==soma_diagonalsecund==soma_linha==soma_coluna[0]==soma_coluna[1]==soma_coluna[2]:
    print(f"É um quadrado magico de soma={soma_coluna[1]}")



  