A , B = map(int,input().split())

isContain = False
for i in (A, B+1):
    if 100 % i == 0:
        isContain = True

if isContain:
    print("Yes")
else:
    print("No")