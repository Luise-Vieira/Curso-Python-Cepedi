tupla=(1,2,4,6,8,9,0,10,12,45)
menor=0
maior=0
for i in range(len(tupla)):
    if i>maior:
        maior=i
    if i<menor:
        menor=i

print(f"O maior é {maior} e o menor é {menor}")

