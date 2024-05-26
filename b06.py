N = int(input())

list_kuji = list(map(int,input().split()))

Q = int(input())

list_atari_sum = [0 for i in range ( N + 1)]
list_hazure_sum = [0 for i in range ( N + 1)]

for i in range (1 , N + 1):
    if list_kuji[i - 1] == 1:
        list_atari_sum[i] = list_atari_sum[i - 1] + 1
        list_hazure_sum[i] = list_hazure_sum[i - 1]
    else:
        list_hazure_sum[i] = list_hazure_sum[i - 1] + 1
        list_atari_sum[i] = list_atari_sum[i - 1]

for i in range (Q):
    A , B = map(int,input().split())
    atari = list_atari_sum[B] - list_atari_sum[A - 1]
    hazure = list_hazure_sum[B] - list_hazure_sum[A - 1]
    if (atari > hazure):
        print("win")
    elif (atari < hazure):
        print("lose")
    else:
        print("draw")
