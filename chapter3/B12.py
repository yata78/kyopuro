import math

N = int(input())

left = 1
right = 100

def check(x):
    return x**3 + x

while left < right:
    middle = math.floor((left + right) / 2)
    if check(middle) > N:
        right = middle
    else:
        left = middle

print('{:.6f}'.format(mid))

