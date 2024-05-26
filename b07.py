T = int(input())
N = int(input())

ruisekihi = [0 for i in range (T + 2)]
goukei = [0 for i in range (T + 2)]

for i in range (N):
    A , B = map(int,input().split())
    ruisekihi[A] = ruisekihi[A] + 1
    ruisekihi[B] = ruisekihi[B] - 1

goukei[0] = ruisekihi[0]

for i in range (1 , T):
    goukei[i] = goukei[i - 1] + ruisekihi[i]

for i in range (T):
    print(goukei[i])