import math

N , X = map(int,input().split())

A_list = list(map(int,input().split()))

left = 0
right = N - 1

flg = True

while flg:
    middle = math.floor((left + right) / 2)
    if (A_list[middle] > X):
        right = middle - 1
    elif (A_list[middle] < X):
        left = middle + 1
    else:
        flg = False

print(middle + 1)