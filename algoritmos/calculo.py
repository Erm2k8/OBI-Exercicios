"""
NÍVEL 2 | 2021 | FASE 2 | CÁLCULO RÁPIDO

Exercício: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/calculo/
"""

S: int = int(input())
A: int = int(input())
B: int = int(input())

# Quantidade de números que somam caracteres igual a S
qtd: int = 0

for i in range(A, B+1):
    # Separa o número em uma lista de caracteres
    s: list[str] = []
    for j in str(i):
        s.append(int(j))

    # Se a soma dos caracteres for igual ao S, é acrescentado 1
    if sum(s) == S:
        qtd += 1

print(qtd)