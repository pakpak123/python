print(" Fun with Drawing ")

n = int(input("Enter input : "))
value = n
size = (2*n)-1

a = [[0 for i in range(size)]for j in range(size)]

for i in range(n):
    for j in range(i,size-i):
        a[i][j] = value
        a[size-i-1][j] = value
        a[j][i] = value
        a[j][size-i-1] = value
    value-=1

for i in range(size) :
    for j in range(size):
        print(a[i][j],end=" ")
    print()