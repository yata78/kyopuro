N = int(input())
answer = ""

for i in range(10):
    wari = 2**i
    answer = str((N // wari) % 2) + answer 

print(answer)