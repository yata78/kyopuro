N , X = map(int,input().split())

list_a = list(map(int, input().split()))

isContain = False

for i in range(N):
  if list_a[i] == X:
    isContain = True
    
if isContain:
  print("Yes")
else:
  print("No")