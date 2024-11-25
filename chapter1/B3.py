N = int(input())

A_list = list(map(int,input().split()))

answer = False

for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1 , N):
            if (A_list[i] + A_list[j] + A_list[z] == 1000):
                answer = True
                break
        if answer:
            break
    if answer:
        break

if answer:
    print("Yes")
else:
    print("No")