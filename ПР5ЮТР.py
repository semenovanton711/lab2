k = int(input())
S=0
f = 1
for i in range(1, k + 1):
    f = f * i
    S = S + (1 / f)
print(S)
