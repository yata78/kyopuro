D = int(input())
N = int(input())

L = [0] * (N + 1)
R = [0] * (N + 1)

for i in range(N):
    L[i], R[i] = map(int,input().split())

zenjituhi = [0] * (D + 2)
ruikei = [0] * (D + 2)

for i in range(N):
    zenjituhi[L[i]] = zenjituhi[L[i]] + 1
    zenjituhi[R[i] + 1] = zenjituhi[R[i] + 1] - 1

for i in range(1 , D + 1):
    ruikei[i] = ruikei[i - 1] + zenjituhi[i]

for i in range(1 , D + 1):
    print(ruikei[i])