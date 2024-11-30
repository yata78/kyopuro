H , W = map(int,input().split())

X = [list(map(int,input().split())) for i in range(H)]

Q = int(input())

A = [0] * Q
B = [0] * Q
C = [0] * Q
D = [0] * Q

for i in range(Q):
    A,B,C,D = map(int,input().split())

#横方向の和を格納するリストを作成
yoko = [[[0] for j in range (W)] for i in range(H)]

for i in range(H):
    for j in range (W):
        if j == 0:
            yoko[i][j] = X[i][j]
        else:
            yoko[i][j] = X[i][j] + yoko[i][j - 1]

#縦方向の和を格納するリストを作成
tate = [[ [0] for j in range (W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if j == 0:
            tate[i][j] = X[i][j]
        else:
            tate[i][j] = tate[i][j - 1] + yoko[i][j]

for i in range(Q):
    print(tate[C - 1][D - 1] - tate[A - 1][D - 1] - tate[C - 1][B - 1] + tate[A - 1][B - 1])