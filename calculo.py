S = int(input())
A = int(input())
B = int(input())

qtd = 0

for i in range(A, B+1):
    s = []
    for j in str(i):
        s.append(int(j))

    if sum(s) == S:
        qtd += 1

print(qtd)
