import bisect

N = int(input())
A_list = list(map(int,input().split()))
Q = int(input())
Z = [None] * Q
for i in range(Q):
    Z[i] = int(input())

# リストをソート
A_list.sort()

for i in range(Q):
    print(bisect.bisect_left(A_list,Z[i]))
