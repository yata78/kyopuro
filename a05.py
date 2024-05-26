N , K = map(int,input().split())

count = 0

for i in range (1, N + 1):
    for j in range (1, N + 1):
        if ((K - (i + j) <= N) and (K - (i + j) > 0)):
                count = count + 1

print(count)