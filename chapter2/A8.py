H , W = map(int,input().split())

X = [list(map(int,input().split())) for i in range(H)]

Q = int(input())

A = [0] * Q
B = [0] * Q
C = [0] * Q
D = [0] * Q



#横方向の和を格納するリストを作成
yoko = [[0 for j in range (W + 1)] for i in range(H + 1)]

for i in range(1 , H + 1):
    for j in range (1 , W + 1):
            yoko[i][j] = X[i - 1][j - 1] + yoko[i][j - 1]

#縦方向の和を格納するリストを作成
tate = [[ 0 for j in range (W + 1)] for i in range(H + 1)]

for i in range(1 , H + 1):
    for j in range(1 , W + 1):
            tate[i][j] = tate[i - 1][j] + yoko[i][j]

for i in range(Q):
    A,B,C,D = map(int,input().split())
    print(tate[C][D] - tate[A - 1][D] - tate[C][B - 1] + tate[A - 1][B - 1])