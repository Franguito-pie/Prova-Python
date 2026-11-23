#EXERCÍCIO 1 - VETORES

vetor = []
dmm = 0

for i in range(5):
    r = int(input(f"Digite a quantidade de chamados do {i + 1}º dia útil da semana: "))
    vetor.append(r)

print("\nFeito!")

tcs = sum(vetor)
mcd = sum(vetor) / 5

for i in range(5):
    if r > mcd:
        dmm += 1


print(f"\nTotal de chamados da semana            --- {tcs}")
print(f"Média de chamados diários                --- {mcd}")
print(f"Dia com maior quantidade de chamados     --- {max(vetor)}")
print(f"Dias com chamados acima da média         --- {dmm}")