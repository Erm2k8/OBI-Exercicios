"""
NÍVEL SÊNIOR | 2021 | FASE 3 | OGRO

Exercício: https://olimpiada.ic.unicamp.br/pratique/p1/2020/f2/lesma/
"""

N = int(input()) # Número de dedos a ser representado

saida1 = "I" * N if N else "*"
saida2 = "I" * (N - 5) if 6 <= N else "*"

print(saida1[:5])
print(saida2)   