N , Q = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = [0] * (N + 1)

for i in range (1 , N + 1):
    B_list[i] = B_list[i - 1] + A_list[i-1]

for i in range (Q):
    L , R = map(int,input().split())
    print(B_list[R] - B_list[L - 1])