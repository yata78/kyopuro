N = int(input())
A_list = list(map(int,input().split()))
Q = int(input())

atari_list = [0] * (N + 1)
hazure_list = [0] * (N + 1)
for i in range(N):
    if A_list[i] == 1:
        atari_list[i + 1] = atari_list[i] + 1
        hazure_list[i + 1] = hazure_list[i]
    else:
        atari_list[i + 1] = atari_list[i]
        hazure_list[i + 1] = hazure_list[i] + 1

for i in range(Q):
    L , R = map(int,input().split())
    if (atari_list[R] - atari_list[L - 1] > hazure_list[R] - hazure_list[L -1]):
        print("win")
    elif (atari_list[R] - atari_list[L - 1] == hazure_list[R] - hazure_list[L -1]):
        print("draw")
    else:
        print("lose")