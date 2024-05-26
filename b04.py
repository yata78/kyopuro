N = str(input())

answer = 0

for i in range(len(N)):
    answer = answer + 2 ** i * int(N[len(N) - i - 1])

print(answer)
