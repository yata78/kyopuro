import math

N , K = map(int,input().split())
A_list = list(map(int,input().split()))

left = 0
right = 10**9

def check(x):
    sumCount = 0
    for i in range (N):
        sumCount += math.floor(x / A_list[i])
    if (K <= sumCount):
        return True
    else:
        return False

while left < right:
    middle = math.floor((left + right) /2)
    if (check(middle)):
        right = middle
    else:
        left = middle + 1

print(left)