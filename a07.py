D = int(input())
N = int(input())

ruiseki = [0 for i in range (D + 2)]
zenjituhi = [0 for i in range (D + 2)]

for i in range(N):
    A , B = map(int,input().split())
    zenjituhi[A] = zenjituhi[A] + 1
    zenjituhi[B + 1] = zenjituhi[B + 1] - 1

for i in range (1 , D + 1):
    ruiseki[i] = ruiseki[i - 1] + zenjituhi[i]
    print(ruiseki[i]) 
