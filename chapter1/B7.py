T = int(input())
N = int(input())

L = [0] * (N + 2)
R = [0] * (N + 2)
total = [0] * (T + 2)
afterTime = [0] * (T + 2)

for i in range(N):
    L[i] , R[i] = map(int,input().split())

for i in range(N):
    afterTime[L[i]] += 1
    afterTime[R[i]] -= 1

total[0] = afterTime[0]

for i in range(1 , N):

    total[i] = total[i - 1] + afterTime[i]

for i in range(N):
    print(total[i])