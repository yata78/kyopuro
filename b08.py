N = int(input())

X = [None] * (N)
Y = [None] * (N)


for i in range (N):
    X[i], Y[i] = map(int,input().split())

Q = int(input())

a = [None] * (Q)
b = [None] * (Q)
c = [None] * (Q)
d = [None] * (Q)

for i in range(Q):
    a[i],b[i],c[i],d[i] = map(int,input().split())

Z = [ [0] * (1501) for i in range(1501)]

for i in range(N):
    Z[X[i]][Y[i]] += 1

S = [ [0] * (1501) for i in range(1501)]

# よこの累積和
for i in range(1 , 1501):
    for j in range(1, 1501):
        S[i][j] = Z[i][j] + S[i][j - 1]

# たての累積和
for i in range(1 , 1501):
    for j in range(1 , 1501):
        S[i][j] = S[i - 1][j] + S[i][j]

for i in range(Q):
    print(S[c[i]][d[i]] + S[a[i] - 1][b[i] - 1] - S[c[i]][b[i] - 1] - S[a[i] - 1][d[i]])