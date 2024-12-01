H,W,N = map(int,input().split())

Z = [[0 for i in range (W + 2)] for j in range(H + 2)]

A = [None] * (N)
B = [None] * (N)
C = [None] * (N)
D = [None] * (N)

for i in range(N):
    A[i],B[i],C[i],D[i] = map(int,input().split())

# 計算の元となるマスに数字を入れていく

for i in range(N):
    Z[A[i]][B[i]] += 1
    Z[A[i]][D[i] + 1] -= 1
    Z[C[i] + 1][B[i]] -= 1
    Z[C[i] + 1][D[i] + 1] += 1

# 横の累積和を計算する
for i in range(1 , H+1):
    for j in range(1 , W+1):
        Z[i][j] += Z[i][j - 1]

# 縦の累積和を計算する
for i in range(1 , H + 1):
    for j in range(1, W + 1):
        Z[i][j] += Z[i - 1][j]

for i in range (1 , H + 1):
    for j in range (1 , W + 1):
        print(Z[i][j] , end=" ")
    print()

