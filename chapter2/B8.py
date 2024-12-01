N = int(input())
X = [None] * N
Y = [None] * N

for i in range (N):
    X[i], Y[i] = map(int,input().split())

Z = [[ 0 for i in range (1501)] for j in range (1501)]

# 各点を表に記載
for i in  range(N):
    Z[X[i]][Y[i]] += 1

# 横の総和を求める

for i in range(1,1501):
    for j in range(1,1501):
        Z[i][j] = Z[i][j] + Z[i][j - 1]

# 縦の総和を求める
for i in range (1, 1501):
    for j in range(1 , 1501):
        Z[i][j] = Z[i][j] + Z[i-1][j]

Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q

for i in range (Q):
    A[i],B[i],C[i],D[i] = map(int,input().split())

for i in range (Q):
    print(Z[C[i]][D[i]] - Z[A[i] - 1][D[i]] - Z[C[i]][B[i] - 1] + Z[A[i] - 1][B[i] - 1])
