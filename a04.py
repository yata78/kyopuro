N = int(input())

answer = ""

while N > 0:
    answer =str(N % 2) + answer
    N = N // 2

while len(answer) < 10:
    answer = '0' + answer

print(answer)
