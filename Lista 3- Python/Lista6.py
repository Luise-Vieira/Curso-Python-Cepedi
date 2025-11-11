#Lista6&7

gabarito=[]

print("Digite os 6 numeros do gabarito")
for i in range(6):
    num=int(input(f"Digite o {i+1} numero:"))
    gabarito.append(num) #add o numero ao gabarito

for aposta in range(10): #ler as 10 apostas
    print(f"\n Aposta {aposta+1}")
    
    numero_aposta=[] #Guardar apostas
    acertos=0
    for j in range(6):
        n=int(input(f"Digite o {j+1} numero da aposta "))
        numero_aposta.append(n)

    for n in numero_aposta: #conta os acertos da aposta
        if n in gabarito: #if n==gabarito[i]
            acertos+=1
    print(f"Total de acertos: {acertos}")

    if acertos==4:
        print("fez a quadra (4 acertos),")
    elif acertos==5:
        print("Fez a quina (5 acertos)")
    elif acertos==6:
        print("sena (6 acertos).")
    else:
        print("Você não ganha nada :( ")