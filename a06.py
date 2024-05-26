N , Q = map(int,input().split())

list_A = list(map(int,input().split()))

list_S = [0 for i in range (N + 1)]

for i in range (1,N + 1):
    list_S[i] = list_S[i - 1] + list_A[i - 1]

for i in range (Q):
    A , B = map(int,input().split())
    print(list_S[B] - list_S[A - 1])
