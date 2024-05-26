N = int(input())

list_a = list(map(int,input().split()))

isContain = False

for i in range(N):
    for j in range(i+1 , N):
        for z in range(j+1 , N):
            if list_a[i] + list_a[j] + list_a[z] == 1000:
                isContain = True

if isContain:
    print("Yes")
else:
    print("No")