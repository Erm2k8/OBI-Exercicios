"""
NÍVEL 1 | 2020 | FASE 2 | DONA LESMA

Exercício: https://olimpiada.ic.unicamp.br/pratique/p1/2020/f2/lesma/
"""

A: int = int(input()) # Altura total
S: int = int(input()) # O quanto ela sobe por dia
D: int = int(input()) # O quanto ela cai de noite

dias: int = 0

#   A é lido como a altura restante
while True:
    A -= S

    dias += 1

    if A <= 0:
        break

    # Se a altura restante não zerar, a contagem continua
    A += D

print(dias)