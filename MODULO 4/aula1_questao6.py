n = int(input())
total = 0
coelhos = 0
ratos = 0
sapos = 0
for _ in range(n):
    q, tipo = input().split()
    q = int(q)
    
    total += q
    
    if tipo == 'C':
        coelhos += q
    elif tipo == 'R':
        ratos += q
    elif tipo == 'S':
        sapos += q
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / total * 100 :.2f} %")
print(f"Percentual de ratos: {ratos / total * 100 :.2f} %")
print(f"Percentual de sapos: {sapos / total * 100 :.2f} %")