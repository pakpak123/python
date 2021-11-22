def insertSort(x)->list:
    for i in range(1,len(x)):
        temp= x[i]
        if temp < 0:
            continue
        for j in range(i,-1,-1):
            if x[j] >= 0:
                n = 1
                while x[j-n] < 0 and j-n >= 0:
                    n += 1
                if temp < x[j-n] and j-n >= 0:
                    x[j] = x[j-n]
                else:
                    x[j] = temp
                    break
    return x

inp = [int(i) for i in input("Enter Input : ").split()]
print(' '.join(map(str,insertSort(inp))))