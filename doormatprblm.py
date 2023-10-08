N,M= map(int, input().split())

l='.|.'
for i in range(N//2):
    p1=(l*((i*2)+1)).center(M,'-')
    print(p1)
print('WELCOME'.center(M,'-'))
for i in range(N//2-1,-1,-1):
    p2=(l*((i*2)+1)).center(M,'-')
    print(p2)
