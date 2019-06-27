N, M = input().split()
L, W = int(N), int(M)
for i in range(1, L, 2):
    print(('.|.' * i).center(W, '-'))
print('WELCOME'.center(W, '-'))
for i in range(L-2 , 0, -2):
    print(('.|.' * i).center(W, '-'))
