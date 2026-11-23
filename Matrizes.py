#EXERCÍCIO 2 - MATRIZES

matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        val = int(input(f"Digite o valor da posição ({i + 1}, {j + 1}): "))
        linha.append(val)
    matriz.append(linha)

cam = matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[0][3]
can = matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[1][3]
bon = matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[2][3]

quim = matriz[0][0] + matriz[1][0] + matriz[2][0]
quit = matriz[0][1] + matriz[1][1] + matriz[2][1]
sexm = matriz[0][2] + matriz[1][2] + matriz[2][2]
sext = matriz[0][3] + matriz[1][3] + matriz[2][3]

tpv = cam + can + bon

mnv = max(cam, can, bon)
pnv = max (quim, quit, sexm, sext)

print(f"\nTotal de vendas para cada produto:")
print(f"Camisetas --- {cam}")
print(f"Canecas   --- {can}")
print(f"Bonés     --- {bon}")

print(f"\nTotal de vendas para cada período:")
print(f"Qui. Manhã   --- {quim}")
print(f"Qui. Tarde   --- {quit}")
print(f"Sex. Manhã   --- {sexm}")
print(f"Sex. Tarde   --- {sext}")

print(f"\nTotal de produtos vendidos:")
print(f"{tpv}")

if mnv == cam:
        print(f"\nCamisetas foram as mais vendidas:")

elif mnv == can:
        print(f"\nCanecas foram as mais vendidas:")

elif mnv == bon:
        print(f"\nBonés foram os mais vendidos:")

if pnv == quit:
    print(f"\nO período mais movimentado foi Quinta de Manhã")

elif pnv == quim:
    print(f"\nO período mais movimentado foi Quinta de Tarde")

elif pnv == sexm:
    print(f"\nO período mais movimentado foi Sexta de Manhã")

elif pnv == sext:
    print(f"\nO período mais movimentado foi Sexta de Tarde")