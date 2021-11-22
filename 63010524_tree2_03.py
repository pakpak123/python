inp = input('Enter Input : ').split('/')
n = int(inp[0])
l = [0]*(n+1)
node = [int(i) for i in inp[1].split()]
len_inp = len(node)
if (n - len_inp)*2+1 == n:
    for i in range(len_inp):
        l[len_inp+i] = node[i]
    for i in range(n-len_inp,0,-1):
        d = min(l[i*2],l[i*2+1])
        l[i] = d
        l[i*2] -= d
        l[i*2+1] -=d
    print(sum(l))
else:
    print('Incorrect Input')